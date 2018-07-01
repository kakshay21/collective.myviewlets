# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.myviewlets.testing import COLLECTIVE_MYVIEWLETS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.myviewlets is properly installed."""

    layer = COLLECTIVE_MYVIEWLETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.myviewlets is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.myviewlets'))

    def test_browserlayer(self):
        """Test that ICollectiveMyviewletsLayer is registered."""
        from collective.myviewlets.interfaces import (
            ICollectiveMyviewletsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveMyviewletsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_MYVIEWLETS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.myviewlets'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.myviewlets is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.myviewlets'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveMyviewletsLayer is removed."""
        from collective.myviewlets.interfaces import \
            ICollectiveMyviewletsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveMyviewletsLayer,
            utils.registered_layers())
