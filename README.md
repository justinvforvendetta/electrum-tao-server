![electrum-tao-server](https://raw.githubusercontent.com/justinvforvendetta/electrum-tao-server/master/splash.png)
Electrum-Tao-Server for the Electrum client
=========================================

  * Original Author: Thomas Voegtlin (ThomasV on the bitcointalk forum)
  * Tao codebase port Author: Sunerok
  * Language: Python

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * All of Tao's OP_CODES for present and future features to be incorporated into transactions/etc

  * The server requires taod, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Tao addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-tao-server' script


License
-------

Electrum-server and Electrum-tao-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
