#!/usr/bin/python
# coding=utf-8

import click

@click.group()
def cli():
	"""CRYPT CLI"""
	pass

@cli.command()
@click.argument('file')
def encrypt(file):
	from util.crypt.crypt_all import crypt_file	
	crypt_file(file,None,debug=True)

@cli.command()
@click.argument('file')
def uncrypt(file):
	from util.crypt.crypt_all import uncrypt_file	
	uncrypt_file(file,None,debug=True)

if __name__ == "__main__":
	cli()
