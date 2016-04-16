[![Build Status](https://travis-ci.org/maruina/ansible-playbooks.svg?branch=master)](https://travis-ci.org/maruina/ansible-playbooks)

# Usage
```bash
ansible-galaxy install -r requirements.yml --force
ansible-playbook --vault-password-file ~/.ssh/vault.txt site.yml
```

# Playbook
1. Convert Debian 7 (Wheezy) into Devuan
2. Configure the system
