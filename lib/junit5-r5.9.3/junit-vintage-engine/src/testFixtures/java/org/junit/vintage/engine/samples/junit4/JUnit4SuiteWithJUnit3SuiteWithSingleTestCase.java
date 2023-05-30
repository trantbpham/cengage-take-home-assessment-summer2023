/*
 * Copyright 2015-2023 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * https://www.eclipse.org/legal/epl-v20.html
 */

package org.junit.vintage.engine.samples.junit4;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;
import org.junit.vintage.engine.samples.junit3.JUnit3SuiteWithSingleTestCaseWithSingleTestWhichFails;

/**
 * @since 4.12
 */
@RunWith(Suite.class)
@SuiteClasses(JUnit3SuiteWithSingleTestCaseWithSingleTestWhichFails.class)
public class JUnit4SuiteWithJUnit3SuiteWithSingleTestCase {
}
