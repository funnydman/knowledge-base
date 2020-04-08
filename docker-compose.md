# https://github.com/docker/compose/issues/4189
To reiterate what I wrote earlier in this thread:

* The environment and env_file sections of the Compose file declare variables that will be available inside the container.
* Variables written using the $VAR or ${VAR} syntax inside the Compose file are replaced by the value found on the host machine (i.e. the machine you're executing docker-compose from) at the time of execution. They're found either in the OS's environment or the statically named .env file.
* If variable substitution is not desired, one should use the double-dollar-sign notation ($$VAR or $${VAR}) to escape the sequence.
