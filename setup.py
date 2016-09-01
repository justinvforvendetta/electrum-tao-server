from setuptools import setup

setup(
    name="electrum-tao-server",
    version="0.9",
    scripts=['run_electrum_tao_server','electrum-tao-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11', 'coinhash>=1.1.5'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'
    ],
    description="Tao Electrum Server",
    author="Thomas Voegtlin, ELM4ever, Propulsion, Sunerok",
    author_email="thomasv1@gmx.de, Propulsion@DarkcoinTalk.org, justinvforvendetta@gmail.com",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/, https://github.com/justinvforvendetta/electrum-tao-server/",
    long_description="Tao electrum server"
)


