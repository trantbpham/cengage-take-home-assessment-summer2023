/*
 * Copyright 2015-2023 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * https://www.eclipse.org/legal/epl-v20.html
 */

package org.junit.platform.launcher.core;

import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.LauncherDiscoveryListener;
import org.junit.platform.launcher.TestExecutionListener;

/**
 * @since 1.8
 */
interface InternalLauncher extends Launcher {

	ListenerRegistry<TestExecutionListener> getTestExecutionListenerRegistry();

	ListenerRegistry<LauncherDiscoveryListener> getLauncherDiscoveryListenerRegistry();
}
