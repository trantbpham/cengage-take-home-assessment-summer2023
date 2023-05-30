/*
 * Copyright 2015-2023 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * https://www.eclipse.org/legal/epl-v20.html
 */

package org.junit.platform.commons.util;

import static java.util.Collections.emptyMap;

import java.io.Closeable;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;

/**
 * @since 1.0
 */
final class CloseablePath implements Closeable {

	private static final String FILE_URI_SCHEME = "file";
	private static final String JAR_URI_SCHEME = "jar";
	private static final String JAR_FILE_EXTENSION = ".jar";
	private static final String JAR_URI_SEPARATOR = "!";

	private static final Closeable NULL_CLOSEABLE = () -> {
	};

	private static final ConcurrentMap<URI, ManagedFileSystem> MANAGED_FILE_SYSTEMS = new ConcurrentHashMap<>();

	private final Path path;
	private final Closeable delegate;

	static CloseablePath create(URI uri) throws URISyntaxException {
		if (JAR_URI_SCHEME.equals(uri.getScheme())) {
			String[] parts = uri.toString().split(JAR_URI_SEPARATOR);
			String jarUri = parts[0];
			String jarEntry = parts[1];
			return createForJarFileSystem(new URI(jarUri), fileSystem -> fileSystem.getPath(jarEntry));
		}
		if (uri.getScheme().equals(FILE_URI_SCHEME) && uri.getPath().endsWith(JAR_FILE_EXTENSION)) {
			return createForJarFileSystem(new URI(JAR_URI_SCHEME + ':' + uri),
				fileSystem -> fileSystem.getRootDirectories().iterator().next());
		}
		return new CloseablePath(Paths.get(uri), NULL_CLOSEABLE);
	}

	private static CloseablePath createForJarFileSystem(URI jarUri, Function<FileSystem, Path> pathProvider) {
		ManagedFileSystem managedFileSystem = MANAGED_FILE_SYSTEMS.compute(jarUri,
			(__, oldValue) -> oldValue == null ? new ManagedFileSystem(jarUri) : oldValue.retain());
		Path path = pathProvider.apply(managedFileSystem.fileSystem);
		return new CloseablePath(path,
			() -> MANAGED_FILE_SYSTEMS.compute(jarUri, (__, ___) -> managedFileSystem.release()));
	}

	private CloseablePath(Path path, Closeable delegate) {
		this.path = path;
		this.delegate = delegate;
	}

	public Path getPath() {
		return path;
	}

	@Override
	public void close() throws IOException {
		delegate.close();
	}

	private static class ManagedFileSystem {

		private final AtomicInteger referenceCount = new AtomicInteger(1);
		private final FileSystem fileSystem;
		private final URI jarUri;

		ManagedFileSystem(URI jarUri) {
			this.jarUri = jarUri;
			try {
				fileSystem = FileSystems.newFileSystem(jarUri, emptyMap());
			}
			catch (IOException e) {
				throw new UncheckedIOException("Failed to create file system for " + jarUri, e);
			}
		}

		private ManagedFileSystem retain() {
			referenceCount.incrementAndGet();
			return this;
		}

		private ManagedFileSystem release() {
			if (referenceCount.decrementAndGet() == 0) {
				close();
				return null;
			}
			return this;
		}

		private void close() {
			try {
				fileSystem.close();
			}
			catch (IOException e) {
				throw new UncheckedIOException("Failed to close file system for " + jarUri, e);
			}
		}
	}
}
