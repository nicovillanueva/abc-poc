#!/usr/bin/python3

import glob
import re

def main():
	atks = find_attackers()
	print(atks)
	a = attackers_menu(atks)
	attacker = build_attacker(a.get('path'), a.get('attacker'), None)
	print(attacker)
	attacker.check()
	attacker.setup()
	attacker.run()

def build_attacker(path, classname, arguments):
	""" Receive the path to the module where the class is located,
	the target class to be instantiated, and the arguments it should receive.
	Then load the module, and using the getattr builtin, build and return the motherfucker
	"""
	import importlib, os
	m = importlib.import_module(path.replace(os.sep, '.').replace('.py', ''))
	return getattr(m, classname)(arguments)


def attackers_menu(kriegers):
	print("We found the following available attacks:")
	for i, k in enumerate(sorted(kriegers, key=lambda x: x.get('attacker'))):
		print('- ({}) {} (In file: {})'.format(i, k.get('attacker'), k.get('path')))
	sel = input("Select which one you want to use: ")
	return sorted(kriegers, key=lambda x: x.get('attacker'))[int(sel)]


def find_attackers(path='src/attacks', baseclass='BaseAttack'):
	p = re.compile('class (.+)\({}\):'.format(baseclass))
	attackers = []
	for file in glob.glob('{}/**/*.py'.format(path), recursive=True):  # requires Py3.5
		with open(file) as f:
			for l in iter(f.readlines()):
				g = re.match(p, l)
				if g is not None:
					attackers.append({'path': f.name, 'attacker': g.group(1)})
					f.close()
					continue
	return attackers

if __name__ == '__main__':
	main()
	pass
