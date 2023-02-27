[![tests](https://github.com/boutetnico/ansible-role-elastic-apm-server/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-elastic-apm-server/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.elastic_apm_server-blue.svg)](https://galaxy.ansible.com/boutetnico/elastic_apm_server)

ansible-role-elastic-apm-server
===============================

This role installs and configures [Elastic APM server](https://www.elastic.co/guide/en/apm/server/current/index.html).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                        | Required | Default                       | Choices   | Comments                 |
|---------------------------------|----------|-------------------------------|-----------|--------------------------|
| elastic_apm_server_dependencies | yes      | `[apt-transport-https,gnupg]` | list      |                          |
| elastic_apm_server_use_oss      | yes      | `false`                       | boolean   |                          |
| elastic_apm_server_config       | yes      |                               | dict      | See `defaults/main.yml`. |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-elastic-apm-server

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
