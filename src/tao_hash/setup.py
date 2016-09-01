from distutils.core import setup, Extension

tao_hash_module = Extension('tao_hash',
                                 sources = ['taomodule.c',
                                            'tao.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
                                            'sha3/shavite.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'tao_hash',
       description = 'Bindings for proof of work used by Tao',
       ext_modules = [tao_hash_module])
