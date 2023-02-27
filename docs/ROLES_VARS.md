# Roles variables quick reference

Here you can find all roles variables

## Elasticsearch

| Var   | Default | Desc |
| ------- | ------- | ----------- |
| `disable_firewall`                | `no`       | Disable firewall. Default no, if you want to configure the firewall use another Role. You can disable the firewall setting this variable to yes  |
| `disable_selinux`                | `no`       | Disable SELinux. Default no, if you want to configure SELinux use another Role. You can disable SELinux setting this variable to yes  |
| `elasticsearch_user`                | `elk`       | Elasticsearch system user  |
| `elasticsearch_group`               | `elk`       | Group of the elastic search system user  |
| `elasticsearch_extract_dir`         | `/opt`       | Elastic search extract dir  |
| `elasticsearch_data_dir`            | `/elasticsearch/data`       | Elasticsearch data dir  |
| `elasticsearch_log_dir`             | `/var/log/elasticsearch`       | Elasticsearch log dir  |
| `elasticsearch_pid_dir`             | `/var/run/elasticsearch`       | Elasticsearch pid dir |
| `elasticsearch_conf_dir`            | `/etc/elasticsearch`       | Elasticsearch conf dir  |
| `elasticsearch_certs_dir`           | `/etc/elasticsearch/certs`       | Elasticsearch certificate dir  |
| `elasticsearch_local_certs_dir`     | `~/very_secure_dir`        | Local directory where to store the Elasticsearch certificates |
| `elasticsearch_security_enabled`    | `yes`       | Enable or not the [Elasticsearch security](https://www.elastic.co/guide/en/elasticsearch/reference/current/secure-cluster.html)  |
| `elasticsearch_https_enabled`    | `yes`       | Enable or not the Elasticsearch security [plus secured HTTPS traffic](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup-https.html)  |
| `elasticsearch_ca_password`         | `c4,p4sSw0rd`       | CA password. **CHANGE** this value, is only an example password.  |
| `elasticsearch_ca_filename`         | `elastic_ca.p12`       | CA filename  |
| `elasticsearch_cert_password`       | `cerT,P4Ssw0rD`       | Certificate password. **CHANGE** this value, is only an example password.  |
| `elasticsearch_cert_filename`       | `elastic_keystore.p12`       | Certificate filename |
| `elasticsearch_http_password`       | `htTp4sS2o3d`       | HTTPS certificate password. **CHANGE** this value, is only an example password.  |
| `elasticsearch_http_file`       | `/tmp/elasticsearch-ssl-http.zip`       | Output file for the HTTPS certificate generation script |
| `elasticsearch_bootstrap_password`  | `changeme`       | Elasticsearch [bootstrap password](https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html#bootstrap-elastic-passwords).  **CHANGE** this value, is only an example password. For more informatsion read [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/built-in-users.html#set-built-in-user-passwords)  |
| `elasticsearch_version`             | `8.1.0`       | Elasticsearch version  |
| `elasticsearch_cluster_name`        | `elk-cluster-test`       | Elasticsearch cluster name  |
| `elasticsearch_default_node_roles`        | `list()`       | Default list of [node roles](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html). If the node is a master node  all the [default roles](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html#node-roles) are associeted whit the provisioned node, except the **data** role.|
| `elasticsearch_master_is_also_data_node`        | `no`       | If set to yes, the master node will be also a data node. The role **data** will be associated with the provisioned node.  |
| `elasticsearch_jvm_xmx`             | `256m`       | JVM XMX memory  |
| `elasticsearch_jvm_xms`             | `256m`       | JVM XMS memory  |
| `elasticsearch_subnet`              | `192.168.25.0/24`       | **CHANGE** this value based on your needs. This value is used to determinate the network interface to use if the machine has multiple network interfaces (Eg. Vagrant) |
| `elasticsearch_resolv_mode`         | `dns`       | How the elastic resolve the names, default dns. If set to host the /etc/hosts file will be overwritten  |
| `elasticsearch_users`         | `list()`       | List of dict. List of user with password. This role will set the default password for each user in this list. You can also use [this](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-passwords.html) tool to generate random password. To get the full list of the default password open the [main.yml](defaults/main.yml) |
| `elasticsearch_install_mode`             | `http`       | Download elasticsearch tar form elastic website. If set to local set *elasticsearch_local_tar_path*  to a local path where the tar was previously downloaded |
| `elasticsearch_local_tar_path`             | `''`       | Local path containing the elasticsearch tar  |

## Kibana

| Var   | Default | Desc |
| ------- | ------- | ----------- |
| `kibana_user`                | `elk`       | Kibana system user  |
| `kibana_group`               | `elk`       | Group of the kibana search system user  |
| `kibana_extract_dir`         | `/opt`       | Kibana search extract dir   |
| `kibana_version`             | `8.1.0`       | Kibana version  |
| `kibana_conf_dir`            | `/etc/kibana`       | Kibana data dir  |
| `kibana_log_dir`             | `/var/log/kibana`       | Kibana data dir  |
| `kibana_certs_dir`           | `/etc/kibana/certs`       | Kibana data dir  |
| `kibana_pid_dir`             | `/var/run/kibana`       | Kibana data dir  |
| `kibana_data_dir`            | `/kibana`       | Kibana data dir  |
| `kibana_https_enabled`       | `no`       | Enable or not https for kibana  |
| `kibana_install_mode`        | `local`       | Download kibana tar form elastic website. If set to local set *kibana_local_tar_path*  to a local path where the tar was previously downloaded  |
| `kibana_local_tar_path`          | `''`       | Local path kibana the elasticsearch tar  |
| `elasticsearch_local_certs_dir`  | `~/very_secure_dir`       | Local directory where the Elasticsearch certificates are stored  |
| `elasticsearch_ca_name`          | `elasticsearch-ca.pem`       | Elasticsearch CA name  |
| `elasticsearch_https_enabled`    | `yes`       | Define if the Elasticsearch security [plus secured HTTPS traffic](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup-https.html) is enabled or not  |
| `elasticsearch_security_enabled`    | `yes`       | Define if [Elasticsearch security](https://www.elastic.co/guide/en/elasticsearch/reference/current/secure-cluster.html) is enabled or not |
| `elasticsearch_username`         | `kibana_system`       | Username used to connect to the elastisearch servers  |
| `elasticsearch_password`         | `K1b4nap4sSw0rd`       | password of the *elasticsearch_username*  |
| `elasticsearch_hosts`            | `[]`       | List of elasticsearch server names  |

## Logstash

| Var   | Default | Desc |
| ------- | ------- | ----------- |
| `logstash_group`               | `elk`       | Logstash system user  |
| `logstash_user`                | `elk`       | Group of the Logstash search system user  |
| `logstash_extract_dir`         | `/opt`       | Logstash search extract dir   |
| `logstash_version`             | `8.1.0`       | Logstash version  |
| `logstash_conf_dir`            | `/etc/logstash`       | Logstash data dir  |
| `logstash_log_dir`             | `/var/log/logstash`       | Logstash data dir  |
| `logstash_certs_dir`           | `/etc/logstash/certs`       | Logstash data dir  |
| `logstash_pid_dir`             | `/var/run/logstash`       | Logstash data dir  |
| `logstash_data_dir`            | `/logstash`       | Logstash data dir  |
| `logstash_beats_tcp_port`      | `5044`       | logstash beats tcp listen port  |
| `logstash_tcp_port`            | `5000`       | logstash  tcp listen port  |
| `logstash_install_mode`        | `local`       | Download Logstash tar form elastic website. If set to local set *logstash_local_tar_path*  to a local path where the tar was previously downloaded  |
| `logstash_local_tar_path`          | `''`       | Local path Logstash the elasticsearch tar  |
| `elasticsearch_local_certs_dir`  | `~/very_secure_dir`       | Local directory where the Elasticsearch certificates are stored  |
| `elasticsearch_ca_name`          | `elasticsearch-ca.pem`       | Elasticsearch CA name  |
| `elasticsearch_https_enabled`    | `yes`       | Define if the Elasticsearch security [plus secured HTTPS traffic](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup-https.html) is enabled or not  |
| `elasticsearch_security_enabled`    | `yes`       | Define if [Elasticsearch security](https://www.elastic.co/guide/en/elasticsearch/reference/current/secure-cluster.html) is enabled or not |
| `elasticsearch_username`         | `logstash_system`       | Username used to connect to the elastisearch servers  |
| `elasticsearch_password`         | `l0gst4sHpAssw0rd,`       | password of the *elasticsearch_username*  |
| `elasticsearch_hosts`            | `[]`       | List of elasticsearch server names  |

## Beats

| Var                              | Default     | Desc |
| ------- | ------- | ----------- |
| `beats_user`                     | `elk`       | Beats system user  |
| `beats_group`                    | `elk`       | Group of the beats search system user  |
| `beats_extract_dir`              | `/opt`       | Beats extract dir   |
| `beats_version`                  | `8.1.0`       | Beats version  |
| `beats_monitoring_enabled`       | `no`       | Enable the beats http server for [monitoring purposes](https://www.elastic.co/guide/en/beats/metricbeat/current/metricbeat-module-beat.html)  |
| `filebeat_monitoring_port`       | `5066`       | filebeat http port  |
| `metricbeat_monitoring_port`     | `5067`       | metricbeat http port  |
| `heartbeat_monitoring_port`      | `5068`       | heartbeat http port  |
| `filebeat_conf_dir`              | `/etc/filebeat`       | Filebeat config directory  |
| `filebeat_certs_dir`             | `/etc/filebeat/certs`       |Filebeat certs directory  |
| `filebeat_data_dir`              | `/filebeat`       | Filebeat data directory  |
| `filebeat_log_dir`               | `/var/log/filebeat`       | Filebeat log directory  |
| `filebeat_number_of_shards`      | `1`       | Number of shard for the filebeat index template  |
| `filebeat_number_of_replicas`    | `1`       | Number of replica for the filebeat index template  |
| `metricbeat_conf_dir`            | `/etc/metricbeat`       | Metricbeat config directory  |
| `metricbeat_certs_dir`           | `/etc/metricbeat/certs`       |Metricbeat certs directory  |
| `metricbeat_data_dir`            | `/metricbeat`       | Metricbeat data directory  |
| `metricbeat_log_dir`             | `/var/log/metricbeat`       | Metricbeat log directory  |
| `metricbeat_number_of_shards`    | `1`       | Number of shard for the metricbeat index template  |
| `metricbeat_number_of_replicas`  | `1`       | Number of replica for the metricbeat index template  |
| `heartbeat_conf_dir`             | `/etc/heartbeat`       | Heartbeat config directory  |
| `heartbeat_certs_dir`            | `/etc/heartbeat/certs`       |Heartbeat certs directory  |
| `heartbeat_data_dir`             | `/heartbeat`       | Heartbeat data directory  |
| `heartbeat_log_dir`              | `/var/log/heartbeat`       | Heartbeat log directory  |
| `heartbeat_number_of_shards`     | `1`       | Number of shard for the heartbeat index template  |
| `heartbeat_number_of_replicas`   | `1`       | Number of replica for the heartbeat index template  |
| `setup_kibana_dashboards`        | `no`       | Install or not the kibana dashboards  |
| `kibana_url`                     | `''`       | kibana url required for the setup of the dashboards  |
| `elasticsearch_local_certs_dir`  | `~/very_secure_dir`       | Local directory where the Elasticsearch certificates are stored  |
| `elasticsearch_ca_name`          | `elasticsearch-ca.pem`       | Elasticsearch CA name  |
| `elasticsearch_https_enabled`    | `yes`       | Define if the Elasticsearch security [plus secured HTTPS traffic](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-basic-setup-https.html) is enabled or not  |
| `elasticsearch_security_enabled`    | `yes`       | Define if [Elasticsearch security](https://www.elastic.co/guide/en/elasticsearch/reference/current/secure-cluster.html) is enabled or not |
| `elasticsearch_username`         | `kibana_system`       | Username used to connect to the elastisearch servers  |
| `elasticsearch_password`         | `K1b4nap4sSw0rd`       | password of the *elasticsearch_username*  |
| `elasticsearch_hosts`            | `[]`       | List of elasticsearch server names  |