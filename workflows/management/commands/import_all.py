from unicodedata import category
from django.core.management.base import BaseCommand, CommandError
from workflows.models import Category, AbstractWidget, AbstractInput, AbstractOutput, AbstractOption
from django.core import serializers
from optparse import make_option
import uuid
import os
import sys
from django.conf import settings
import json
from .import_package import import_package

class Command(BaseCommand):
    args = 'package_name'
    help = 'Imports all packages.'

    def handle(self, *args, **options):
        packages = []
        for app in settings.INSTALLED_APPS:
            if 'workflows.' in app:
                packages.append(app)

        for package in packages:
            package_name = package.split('workflows.')[1]
            self.stdout.write("Importing package "+package_name+"\n")
            import_package(package_name,self.stdout)