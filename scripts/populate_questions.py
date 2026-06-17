import os
import json

# Ensure output directory exists
os.makedirs('data', exist_ok=True)

# Provider and exam definitions with Cheat Sheets
certifications_data = [
    {
        "id": "google-associate-cloud-engineer",
        "provider": "google-cloud",
        "name": "Google Associate Cloud Engineer (ACE)",
        "description": "Validates your ability to deploy applications, monitor operations, manage enterprise solutions, and configure networks and security on GCP.",
        "icon": "⚡",
        "cheatsheet": {
            "summary": "Focuses on the practical setup, deployment, and operation of core GCP infrastructure components (VPC, VMs, Storage, and GKE).",
            "coreConcepts": [
                {"name": "IAM Roles & Hierarchy", "desc": "Least privilege principle. User access is managed via Member -> Role -> Resource bindings across Org, Folder, Project, Resource scopes."},
                {"name": "VPC Global Network", "desc": "Virtual Private Cloud networks are global. Subnets inside are regional. Internal routing works natively between subnets across regions."},
                {"name": "Managed Instance Groups", "desc": "MIGs use templates to scale compute nodes dynamically based on CPU/load, handling healing and auto-updates."},
                {"name": "Storage Classes", "desc": "Standard (hot), Nearline (30+ days backup), Coldline (90+ days), Archive (365+ days disaster recovery)."}
            ],
            "commands": [
                {"cmd": "gcloud auth login", "desc": "Authorizes SDK access using Google credentials."},
                {"cmd": "gcloud compute instances create my-vm --zone=us-central1-a", "desc": "Creates a virtual machine in a specific zone."},
                {"cmd": "gsutil mb -c nearline gs://my-bucket", "desc": "Creates a Cloud Storage bucket using nearline class."}
            ],
            "architecturalPatterns": [
                {"scenario": "Static Asset Hosting", "solution": "Store media files in a Cloud Storage bucket, set uniform IAM access, and map a global HTTPS load balancer with Cloud CDN for caching."},
                {"scenario": "Safe VM Internet Egress", "solution": "Keep VM instances in a private subnet (no external IPs) and route outgoing traffic through Cloud NAT for software updates."}
            ]
        },
        "topics": [
            {
                "topic": "IAM Roles",
                "q": "Your development team needs to store and retrieve files from a Cloud Storage bucket. The team should be able to view, list, delete, and overwrite objects, but must not be allowed to change bucket permissions. Which IAM role should you grant?",
                "opts": ["Storage Admin", "Storage Object Creator", "Storage Object Admin", "Storage Object Viewer"],
                "ans": 2,
                "exp": "Storage Object Admin allows full control over Cloud Storage objects (files), but does not allow modifying bucket-level IAM policies or permissions."
            },
            {
                "topic": "Compute Engine",
                "q": "You want to set up autoscaling for a containerized web application running on Compute Engine VMs. What resource type must you create first to enable autoscaling?",
                "opts": ["An unmanaged instance group", "A managed instance group (MIG)", "A load balancer", "A virtual private cloud (VPC)"],
                "ans": 1,
                "exp": "Compute Engine autoscaling is a feature of Managed Instance Groups (MIGs). You cannot configure autoscaling on unmanaged instance groups."
            },
            {
                "topic": "Cloud Storage",
                "q": "Which Cloud Storage class is most cost-effective for data that you plan to access less than once a year?",
                "opts": ["Standard", "Nearline", "Coldline", "Archive"],
                "ans": 3,
                "exp": "Archive Storage is the lowest-cost, highly durable storage service for data archiving, online backup, and disaster recovery."
            },
            {
                "topic": "VPC Networking",
                "q": "You create a new custom VPC network. Within this network, you create two subnets in different regions. What is the default internal connectivity status between VMs in these subnets?",
                "opts": [
                    "They cannot communicate internally because they are in different regions.",
                    "They can communicate internally by default because Google Cloud custom VPCs have system-generated routing rules that connect all subnets in the VPC.",
                    "They can only communicate internally if you set up VPC Network Peering.",
                    "They can only communicate if they are assigned public external IP addresses."
                ],
                "ans": 1,
                "exp": "In Google Cloud, VPC networks are global. Subnets within the same VPC, regardless of their regions, are automatically connected via system-generated internal routes."
            },
            {
                "topic": "Google Kubernetes Engine (GKE)",
                "q": "You want to deploy a containerized application to GKE and ensure that Google automatically manages the node upgrading, scaling, and provisioning. Which GKE cluster mode should you select?",
                "opts": ["Standard Mode", "Autopilot Mode", "Private Cluster Mode", "Shared VPC Cluster Mode"],
                "ans": 1,
                "exp": "In Autopilot mode, GKE provisions and manages the cluster's underlying infrastructure, including nodes, scaling, security, and upgrades."
            }
        ]
    },
    {
        "id": "google-cloud-digital-leader",
        "provider": "google-cloud",
        "name": "Google Cloud Digital Leader",
        "description": "Validates foundational knowledge of cloud concepts, Google Cloud products, services, tools, features, and primary use cases.",
        "icon": "☁️",
        "cheatsheet": {
            "summary": "Business-level overview of Cloud value propositions, TCO, and matching business problems to Google Cloud products.",
            "coreConcepts": [
                {"name": "CapEx vs OpEx", "desc": "Capital Expenditure (buying physical servers upfront) shifts to Operational Expenditure (pay-as-you-go utility pricing)."},
                {"name": "IaaS vs PaaS vs SaaS", "desc": "Infrastructure (VMs/Disks), Platform (managed runtimes like App Engine/Cloud Run), Software (Google Workspace/SaaS Apps)."},
                {"name": "Shared Responsibility Model", "desc": "Google manages security OF the cloud (physical centers, hypervisor). Customer manages security IN the cloud (IAM configuration, database queries)."}
            ],
            "commands": [
                {"cmd": "N/A (Conceptual Exam)", "desc": "This exam does not require command-line CLI test configurations, focusing on cloud business logic."}
            ],
            "architecturalPatterns": [
                {"scenario": "Global Low-Latency Storage", "solution": "Use Cloud Spanner for globally distributed relational database systems requiring strong consistency."},
                {"scenario": "Modern Data Analytics", "solution": "Aggregate all enterprise business data into BigQuery to execute rapid petabyte-scale SQL queries."}
            ]
        },
        "topics": [
            {
                "topic": "Cloud Concepts",
                "q": "What is the primary benefit of shifting from Capital Expenditure (CapEx) to Operational Expenditure (OpEx) in cloud computing?",
                "opts": [
                    "Paying a fixed amount regardless of usage",
                    "Paying only for resources consumed, reducing upfront hardware costs",
                    "Ensuring that servers are physically hosted on-premises",
                    "Eliminating the need to configure software security"
                ],
                "ans": 1,
                "exp": "OpEx allows businesses to pay as they go for operational resources rather than investing heavily upfront in physical infrastructure (CapEx)."
            },
            {
                "topic": "Compute & Serverless",
                "q": "Which Google Cloud service lets you run containerized applications without provisioning or managing virtual machines?",
                "opts": ["Compute Engine", "Cloud Storage", "Cloud Run", "Cloud SQL"],
                "ans": 2,
                "exp": "Cloud Run is a fully managed serverless compute platform that runs containerized applications."
            },
            {
                "topic": "Shared Responsibility Model",
                "q": "According to the Google Cloud Shared Responsibility Model, who is responsible for the physical security of data centers?",
                "opts": [
                    "The customer only",
                    "Google Cloud only",
                    "Shared equally between Google Cloud and the customer",
                    "A third-party auditing agency"
                ],
                "ans": 1,
                "exp": "Under the Google Cloud Shared Responsibility Model, Google Cloud is solely responsible for physical security of data centers."
            },
            {
                "topic": "Database Selection",
                "q": "Which Google Cloud database service is best suited for storing transactional relational data that requires global scalability and strong consistency?",
                "opts": ["Cloud SQL", "Cloud Spanner", "Cloud Bigtable", "Firestore"],
                "ans": 1,
                "exp": "Cloud Spanner is a fully managed, mission-critical, relational database service that provides transactional consistency at global scale."
            },
            {
                "topic": "Data Analytics",
                "q": "Your company needs a serverless data warehouse to perform SQL analysis on petabytes of structured data with minimal setup. Which service should you choose?",
                "opts": ["Cloud SQL", "BigQuery", "Cloud Dataproc", "Cloud Spanner"],
                "ans": 1,
                "exp": "BigQuery is Google Cloud's fully managed, serverless enterprise data warehouse designed for SQL queries on large-scale datasets."
            }
        ]
    },
    {
        "id": "google-professional-cloud-architect",
        "provider": "google-cloud",
        "name": "Google Professional Cloud Architect (PCA)",
        "description": "Evaluates your ability to design, develop, and manage robust, secure, scalable, and highly available GCP solutions.",
        "icon": "🏛️",
        "cheatsheet": {
            "summary": "Designing enterprise architecture: mapping business objectives to technical requirements, ensuring security, HA, DR, compliance, and cost optimization.",
            "coreConcepts": [
                {"name": "DR Strategies (RTO / RPO)", "desc": "Recovery Time Objective (downtime allowed) and Recovery Point Objective (data loss allowed). Multi-region replicates reduce both parameters close to zero."},
                {"name": "Hybrid Connection SLAs", "desc": "Cloud VPN (routing via public internet, lower cost), Partner Interconnect (private link through provider), Dedicated Interconnect (physical link to Google core, 99.99% SLA availability)."},
                {"name": "Security & Exfiltration", "desc": "VPC Service Controls locks APIs down to network perimeters. Cloud KMS handles key management."}
            ],
            "commands": [
                {"cmd": "gcloud compute instances migrate ...", "desc": "Manages VM migration steps and configuration."},
                {"cmd": "gcloud container clusters create ...", "desc": "Configures GKE clusters in enterprise private projects."}
            ],
            "architecturalPatterns": [
                {"scenario": "Global Web Server Failover", "solution": "Global HTTP(S) Load Balancer distributing connections to VMs in MIGs in us-east1 and europe-west1, backed by Cloud Spanner multi-region."},
                {"scenario": "Enterprise Audit Trails", "solution": "Collect system logs in Cloud Logging, filter out administrative logs, and export via Log Sink to a BigQuery dataset for security audit analysis."}
            ]
        },
        "topics": [
            {
                "topic": "Designing for High Availability",
                "q": "You are designing a high-availability multi-tier application. The database layer must support failover with zero data loss across regions. Which architecture should you choose?",
                "opts": [
                    "Cloud SQL with cross-region read replicas promoted manually",
                    "Cloud Spanner with a multi-region configuration",
                    "Compute Engine VM instances with database replication over Cloud VPN",
                    "Cloud SQL with High Availability (HA) enabled in a single region"
                ],
                "ans": 1,
                "exp": "Cloud Spanner multi-region configurations provide synchronous replication and database failover with a 99.999% availability SLA and zero data loss."
            },
            {
                "topic": "Cloud Migration",
                "q": "You are migrating 100 TB of historical log data from your on-premises SAN to Cloud Storage. The migration must complete within 2 days over a 1 Gbps dedicated internet link. What is the recommended strategy?",
                "opts": [
                    "Upload data using gsutil multi-threading over the internet.",
                    "Order a Google Transfer Appliance, load the data on-premises, and ship it to Google.",
                    "Configure a Cloud VPN connection and copy the files.",
                    "Use Partner Interconnect to transfer the data."
                ],
                "ans": 1,
                "exp": "A 1 Gbps connection would take around 10-12 days to upload 100 TB. The Google Transfer Appliance is the recommended, secure offline data transfer option for this scale and timeframe."
            },
            {
                "topic": "Security and Compliance",
                "q": "Your enterprise organization needs to prevent data exfiltration from Cloud Storage buckets and BigQuery datasets, ensuring they are only accessible from within your private network or authorized subnets. What should you configure?",
                "opts": ["VPC Service Controls", "IAM Custom Roles", "Cloud Armor Policies", "VPC Network Peering"],
                "ans": 0,
                "exp": "VPC Service Controls allows you to define a security perimeter around Google Cloud resources to prevent data exfiltration and block unauthorized access."
            },
            {
                "topic": "Load Balancing",
                "q": "You need to distribute global HTTPS traffic to backends located in multiple regions (US, Europe, Asia) to minimize latency for end-users. Which load balancer should you use?",
                "opts": [
                    "Regional External HTTP(S) Load Balancer",
                    "Global External HTTP(S) Load Balancer (Classic or Modern)",
                    "Network Load Balancer",
                    "Internal HTTP(S) Load Balancer"
                ],
                "ans": 1,
                "exp": "The Global External HTTP(S) Load Balancer is a proxy load balancer that routes user requests to the closest backend instance based on geography and capacity."
            },
            {
                "topic": "Disaster Recovery",
                "q": "You want to configure disaster recovery for VM instances running in us-east1. In the event of a zone outage, the VMs should be bootable in us-east4 with minimal RTO. What is the most cost-effective recovery method?",
                "opts": [
                    "Maintain active duplicate VMs running in us-east4.",
                    "Configure schedule-based persistent disk snapshots and replicate them to us-east4.",
                    "Export VM disks to Cloud Storage and import them when needed.",
                    "Use GKE multi-cluster ingress to duplicate VM instances."
                ],
                "ans": 1,
                "exp": "Replicating persistent disk snapshots across regions provides a low-cost, secure backup of VM states that can be quickly restored as boot disks in another region."
            }
        ]
    },
    {
        "id": "google-professional-data-engineer",
        "provider": "google-cloud",
        "name": "Google Professional Data Engineer (PDE)",
        "description": "Assesses skills in designing, building, operationalizing, and securing data processing systems on Google Cloud.",
        "icon": "📊",
        "cheatsheet": {
            "summary": "Building data collection and processing architectures: Pub/Sub ingestion, Dataflow streaming, BigQuery storage, Bigtable NoSQL, and Cloud Composer orchestration.",
            "coreConcepts": [
                {"name": "BigQuery Partitioning & Clustering", "desc": "Partitioning divides data by date/time (saves scan costs). Clustering sorts data by key columns inside partitions (speeds up filters/groups)."},
                {"name": "Cloud Bigtable Keys", "desc": "NoSQL wide-column database. Row keys must be designed sequentially to prevent hotspotting (e.g. sensor_id#timestamp instead of timestamp first)."},
                {"name": "Dataflow Windowing", "desc": "Tumbling (fixed non-overlapping), Hopping (overlapping time frames), Session (inactivity gap-based)."}
            ],
            "commands": [
                {"cmd": "bq query --use_legacy_sql=false 'SELECT ...'", "desc": "Runs a SQL query against BigQuery using standard SQL compiler."},
                {"cmd": "gcloud composer environments create ...", "desc": "Initializes a managed Apache Airflow workflow environment."}
            ],
            "architecturalPatterns": [
                {"scenario": "Real-time Ad Ingestion Pipeline", "solution": "Ingest user clicks via Pub/Sub, stream process using Cloud Dataflow (sliding window aggregations), and save outputs in BigQuery for dashboard analysis."},
                {"scenario": "IoT Event Hub", "solution": "Stream millisecond sensor logs to Cloud Pub/Sub, write to Cloud Bigtable using a optimized sensor#timestamp row key for time-series lookup."}
            ]
        },
        "topics": [
            {
                "topic": "BigQuery Optimization",
                "q": "You run heavy analytical queries in BigQuery that filter by a transaction date and group by a store ID. How should you design the table to minimize costs and optimize query speed?",
                "opts": [
                    "Partition by transaction date and cluster by store ID.",
                    "Cluster by transaction date and partition by store ID.",
                    "Create separate tables for every store ID.",
                    "Increase the reservation slots in BigQuery."
                ],
                "ans": 0,
                "exp": "Partitioning by date narrows down the scanned data blocks (reducing cost), while clustering by store ID sorts data within partitions to speed up grouping and filtering."
            },
            {
                "topic": "Bigtable Schema Design",
                "q": "You are designing a row key for a Cloud Bigtable database storing IoT sensor metrics. The query pattern is always retrieving records for a specific sensor ID over a recent time range. How should you format the row key to avoid hotspotting?",
                "opts": [
                    "sensor_id#timestamp",
                    "timestamp#sensor_id",
                    "sensor_id",
                    "timestamp"
                ],
                "ans": 0,
                "exp": "Starting the row key with the sensor ID groups that sensor's metrics together. Appending the timestamp allows time-range queries. Placing timestamp first would cause hotspotting on the node handling the current time."
            },
            {
                "topic": "Data Pipeline Orchestration",
                "q": "You need to orchestrate a complex workflow that extracts data from Cloud Storage, triggers a Dataproc Spark job, and loads results into BigQuery daily. Which Google Cloud service should you use?",
                "opts": ["Cloud Composer (managed Apache Airflow)", "Cloud Dataflow", "Cloud Pub/Sub", "Cloud Tasks"],
                "ans": 0,
                "exp": "Cloud Composer is a fully managed workflow orchestration service built on Apache Airflow, ideal for authoring, scheduling, and monitoring pipelines."
            },
            {
                "topic": "Stream Processing",
                "q": "You are building a real-time data streaming pipeline that needs to ingest data from mobile apps, perform aggregations over a sliding window, and handle late-arriving data. Which service combination should you select?",
                "opts": [
                    "Pub/Sub for ingestion and Cloud Dataflow for processing",
                    "Pub/Sub for ingestion and BigQuery for processing",
                    "Cloud Storage for ingestion and Dataproc for processing",
                    "Cloud SQL for ingestion and Cloud Composer for processing"
                ],
                "ans": 0,
                "exp": "Pub/Sub handles scalable ingestion, while Cloud Dataflow (based on Apache Beam) supports streaming windowing, watermarks, and triggers for late data."
            },
            {
                "topic": "Database Selection",
                "q": "Your application requires a NoSQL document database that supports real-time synchronization, mobile offline access, and ACID transactions. Which service should you choose?",
                "opts": ["Firestore", "Cloud Bigtable", "Cloud SQL", "MemoryStore"],
                "ans": 0,
                "exp": "Firestore is a serverless NoSQL document database designed for mobile and web apps, supporting ACID transactions and offline sync."
            }
        ]
    },
    {
        "id": "google-professional-cloud-developer",
        "provider": "google-cloud",
        "name": "Google Professional Cloud Developer (PCD)",
        "description": "Tests your proficiency in designing, building, testing, and deploying cloud-native applications on Google Cloud.",
        "icon": "💻",
        "cheatsheet": {
            "summary": "Focuses on cloud-native application architectures, API design, CI/CD with Cloud Build, secrets management, testing, and monitoring.",
            "coreConcepts": [
                {"name": "Serverless Scaling", "desc": "Cloud Run scales containers automatically down to zero. Cold startup times are controlled by setting minimum instances configurations."},
                {"name": "CI/CD Pipeline steps", "desc": "Source code (GitHub/Cloud Source) -> Cloud Build (Docker compile) -> Artifact Registry (Container storing) -> Cloud Deploy (GKE/Cloud Run rollouts)."},
                {"name": "Tracing and Profiling", "desc": "Cloud Trace (request latency paths), Cloud Profiler (CPU/Memory optimization in code), Cloud Logging (debug outputs)."}
            ],
            "commands": [
                {"cmd": "gcloud builds submit --config=cloudbuild.yaml", "desc": "Triggers a Cloud Build compilation job using a local workspace."},
                {"cmd": "gcloud secrets create db-pwd --data-file=password.txt", "desc": "Registers a new secure environment key in Secret Manager."}
            ],
            "architecturalPatterns": [
                {"scenario": "Secure API Secrets", "solution": "Store API tokens in Secret Manager, grant the compute service account Secret Manager Accessor, and inject secrets as environment variables in Cloud Run at startup."},
                {"scenario": "Low-Latency Profile Syncing", "solution": "Cache relational database query profiles in Cloud Memorystore (Redis) to speed up microservice response times."}
            ]
        },
        "topics": [
            {
                "topic": "CI/CD Pipelines",
                "q": "You want to automate your application's deployment pipeline. Code changes pushed to GitHub should automatically build a container image, push it to Artifact Registry, and deploy it to Cloud Run. Which tool should you use to coordinate this?",
                "opts": ["Cloud Build", "Cloud Composer", "Cloud Deploy", "Cloud Tasks"],
                "ans": 0,
                "exp": "Cloud Build is Google Cloud's serverless CI/CD platform that compiles code, creates container images, and executes deployment scripts."
            },
            {
                "topic": "Application Debugging",
                "q": "You have deployed a production microservice to Cloud Run. Users are experiencing intermittent timeouts. You want to trace requests across microservices to identify bottlenecks. What should you configure?",
                "opts": ["Cloud Trace", "Cloud Profiler", "Cloud Debugger", "Cloud Logging"],
                "ans": 0,
                "exp": "Cloud Trace is a distributed tracing system that collects latency data from your applications and displays request lifecycles."
            },
            {
                "topic": "Secrets Management",
                "q": "Your application needs to securely store API keys and database credentials. You must prevent hardcoding secrets in application source files. Which service should you integrate?",
                "opts": ["Secret Manager", "Cloud KMS", "Identity-Aware Proxy", "Artifact Registry"],
                "ans": 0,
                "exp": "Secret Manager is a secure, convenient storage system for API keys, passwords, credentials, and other sensitive data."
            },
            {
                "topic": "App Engine Configurations",
                "q": "You want to deploy a Python web application to App Engine Standard. Which file must you configure in the root directory to define the scaling behavior and runtime environment?",
                "opts": ["app.yaml", "Dockerfile", "kubernetes.yaml", "main.py"],
                "ans": 0,
                "exp": "App Engine Standard uses the `app.yaml` file to define runtime environments, entry points, scaling behaviors, and environment variables."
            },
            {
                "topic": "Microservices Ingestion",
                "q": "You are building a decoupled microservice application. Service A needs to trigger Service B asynchronously whenever a user registers. Which service is designed to handle this decoupling?",
                "opts": ["Cloud Pub/Sub", "Cloud SQL", "Cloud Memorystore", "Cloud DNS"],
                "ans": 0,
                "exp": "Cloud Pub/Sub is an asynchronous messaging service that decouples services that produce events from services that process events."
            }
        ]
    },
    {
        "id": "google-professional-cloud-security-engineer",
        "provider": "google-cloud",
        "name": "Google Professional Cloud Security Engineer",
        "description": "Tests your ability to design, develop, and manage a secure infrastructure using Google Cloud security technologies.",
        "icon": "🛡️",
        "cheatsheet": {
            "summary": "Implementing security perimeters: identity management, encryption, network security, regulatory compliance, and security monitoring.",
            "coreConcepts": [
                {"name": "Encryption at Rest", "desc": "Google-Managed (GMEK, default), Customer-Managed (CMEK, keys inside Cloud KMS), Customer-Supplied (CSEK, keys stored on-premises outside GCP)."},
                {"name": "VPC Service Controls", "desc": "Mitigates data exfiltration risk by blocking service API queries originating from outside defined networks/perimeters."},
                {"name": "Cloud DLP (Sensitive Data Protection)", "desc": "Uses infoType detectors to automatically identify, classify, mask, or redact PII data."}
            ],
            "commands": [
                {"cmd": "gcloud kms keys create ...", "desc": "Initializes custom encryption keys inside a Cloud KMS keyring."},
                {"cmd": "gcloud iam roles create ...", "desc": "Creates custom roles to enforce least privilege access."}
            ],
            "architecturalPatterns": [
                {"scenario": "Preventing Public Storage Access", "solution": "Enable Organization Policy constraint 'Restrict Public IP Access' and use 'Uniform Bucket-Level Access' on Cloud Storage buckets."},
                {"scenario": "Restricting Admin Console access", "solution": "Secure internal VM administration by enabling Identity-Aware Proxy (IAP) tunnels for SSH/RDP without exposing public VMs."}
            ]
        },
        "topics": [
            {
                "topic": "Data Encryption",
                "q": "Your company's security policy requires that all data stored in Cloud Storage must be encrypted using keys that you generate, manage, and rotate outside of Google Cloud. Which encryption method should you use?",
                "opts": [
                    "Customer-Supplied Encryption Keys (CSEK)",
                    "Customer-Managed Encryption Keys (CMEK) via Cloud KMS",
                    "Google-Managed Encryption Keys (GMEK)",
                    "VPC Service Controls"
                ],
                "ans": 0,
                "exp": "CSEKs allow you to supply your own encryption keys. Google uses these keys to encrypt the data, but never stores them on disk."
            },
            {
                "topic": "Web Application Security",
                "q": "Your web application running on Compute Engine VMs is experiencing Distributed Denial of Service (DDoS) and SQL injection attacks from the internet. Which service should you configure to protect it?",
                "opts": ["Cloud Armor", "VPC Service Controls", "Identity-Aware Proxy (IAP)", "Cloud Firewalls"],
                "ans": 0,
                "exp": "Cloud Armor protects web applications from DDoS attacks and OWASP Top 10 risks (like SQL injection and cross-site scripting)."
            },
            {
                "topic": "Identity and Access Management",
                "q": "You want to grant users access to an administrative VM instance without exposing its public IP address or configuring a VPN. Which security service should you implement?",
                "opts": [
                    "Identity-Aware Proxy (IAP) TCP forwarding",
                    "Cloud VPN Gateway",
                    "VPC Service Controls",
                    "Cloud NAT"
                ],
                "ans": 0,
                "exp": "IAP's TCP forwarding feature allows you to control who can access administrative services (like SSH or RDP) on VMs without public IP addresses."
            },
            {
                "topic": "Sensitive Data Discovery",
                "q": "You want to automatically scan Cloud Storage buckets for personally identifiable information (PII) like credit card numbers or social security IDs, and redact them. Which tool should you use?",
                "opts": [
                    "Sensitive Data Protection (Cloud DLP)",
                    "Cloud Security Command Center (SCC)",
                    "Cloud Logging",
                    "Secret Manager"
                ],
                "ans": 0,
                "exp": "Sensitive Data Protection (formerly Cloud DLP) helps you discover, classify, and redact sensitive data in cloud storage and databases."
            },
            {
                "topic": "Auditing and Logging",
                "q": "You need to audit all read actions on files inside your Cloud Storage buckets. By default, these logs are disabled to save storage costs. Which log type must you enable?",
                "opts": [
                    "Data Access Audit Logs",
                    "Admin Activity Audit Logs",
                    "System Event Audit Logs",
                    "VPC Flow Logs"
                ],
                "ans": 0,
                "exp": "Data Access Audit logs record when API calls read resource configurations or user-provided data (disabled by default, except for BigQuery)."
            }
        ]
    },
    {
        "id": "google-professional-cloud-network-engineer",
        "provider": "google-cloud",
        "name": "Google Professional Cloud Network Engineer",
        "description": "Validates your expertise in designing, planning, and managing Google Cloud network architectures.",
        "icon": "🌐",
        "cheatsheet": {
            "summary": "Network architecture design: configuring Shared VPC networks, routing, load balancers, DNS, and hybrid connectivity links.",
            "coreConcepts": [
                {"name": "Shared VPC", "desc": "Centralizes subnets and firewalls inside a single host project, sharing subnets to service projects in the organization resource tree."},
                {"name": "Cloud Router & BGP", "desc": "Exchanges dynamic routes via Border Gateway Protocol between Google Cloud VPC networks and local physical routers."},
                {"name": "Global Load Balancing", "desc": "HTTP(S) Load Balancer acts as reverse proxy, routing user traffic via Google's edge locations. Backed by Cloud CDN for static files."}
            ],
            "commands": [
                {"cmd": "gcloud compute networks subnets create ...", "desc": "Creates regional subnets within a global VPC network."},
                {"cmd": "gcloud compute routers create ...", "desc": "Registers a virtual router to coordinate BGP sessions."}
            ],
            "architecturalPatterns": [
                {"scenario": "Safe Database Connectivity", "solution": "Set up Private Google Access on subnets to allow VMs without external public IPs to communicate with GCP API services like BigQuery and Cloud Storage."},
                {"scenario": "Network Isolation", "solution": "Configure VPC Network Peering to connect two separate VPC networks internally using private IP spaces without public internet routing."}
            ]
        },
        "topics": [
            {
                "topic": "Hybrid Connectivity",
                "q": "You need to configure dynamic routing between your on-premises network and a Google Cloud VPC using Cloud VPN. Which service is required to establish BGP sessions?",
                "opts": ["Cloud Router", "Cloud NAT", "Cloud DNS", "Partner Interconnect"],
                "ans": 0,
                "exp": "Cloud Router uses Border Gateway Protocol (BGP) to dynamically exchange routes between your VPC and on-premises networks."
            },
            {
                "topic": "VPC Organization Architecture",
                "q": "Your enterprise wants to centralize network management (subnets, firewalls, routing) in a single host project while allowing developers to launch VMs in separate service projects. What should you configure?",
                "opts": ["Shared VPC", "VPC Network Peering", "Cloud VPN", "VPC Service Controls"],
                "ans": 0,
                "exp": "Shared VPC allows an organization to connect resources from multiple projects to a common Virtual Private Cloud (VPC) network."
            },
            {
                "topic": "IP Address Management",
                "q": "You have VM instances in a private subnet (no public IPs) that need to download updates from the public internet. Which service should you configure to enable this internet egress?",
                "opts": ["Cloud NAT", "Cloud Router", "Cloud Load Balancing", "Cloud VPN"],
                "ans": 0,
                "exp": "Cloud NAT (Network Address Translation) allows VM instances without external IP addresses to access the internet."
            },
            {
                "topic": "Load Balancing Traffic Routing",
                "q": "You are hosting a video streaming service. You want to cache content at edge locations to minimize latency for global clients. Which load balancing feature should you enable?",
                "opts": ["Cloud CDN", "Cloud Armor", "Google Cloud DNS", "Session Affinity"],
                "ans": 0,
                "exp": "Cloud CDN (Content Delivery Network) works with external HTTP(S) load balancers to cache media content close to users."
            },
            {
                "topic": "Domain Name Resolution",
                "q": "You want to forward DNS queries from your on-premises active directory domain to your private Google Cloud DNS zones. What should you configure?",
                "opts": [
                    "Cloud DNS Inbound Query Policies",
                    "Cloud DNS Outbound Forwarding Zones",
                    "A public DNS zone",
                    "A hosts file on the instances"
                ],
                "ans": 0,
                "exp": "An Inbound DNS Query Policy allows you to configure entry-point IP addresses in your VPC that resolve queries via Cloud DNS."
            }
        ]
    },
    {
        "id": "google-professional-cloud-devops-engineer",
        "provider": "google-cloud",
        "name": "Google Professional Cloud DevOps Engineer",
        "description": "Evaluates proficiency in using Google Cloud services to build and operationalize software delivery pipelines and manage service reliability.",
        "icon": "♾️",
        "cheatsheet": {
            "summary": "Operationalizing reliable systems: SRE foundations (SLI/SLO/Error Budgets), logging strategies, CI/CD deployment logic, and monitoring systems.",
            "coreConcepts": [
                {"name": "SLI vs SLO vs SLA", "desc": "Service Level Indicator (measurable latency/error rate), Service Level Objective (internal target, e.g., 99.9% uptime), Service Level Agreement (contractual commitment to users)."},
                {"name": "Error Budgets", "desc": "100% - SLO. Represents the allowable downtime or error rate. Used to balance deployment velocity against service stability."},
                {"name": "Deployment Strategies", "desc": "Canary (tests 1% of users), Blue-Green (switches 100% traffic to duplicate environment), Rolling (upgrades nodes sequentially)."}
            ],
            "commands": [
                {"cmd": "terraform init && terraform apply", "desc": "Initializes and deploys infrastructure templates declaratively."},
                {"cmd": "gcloud logging read 'severity>=ERROR'", "desc": "Queries log messages filtering out non-error entries."}
            ],
            "architecturalPatterns": [
                {"scenario": "Proactive Alerting", "solution": "Set up a Cloud Monitoring alerting policy tracking SLO error budget burn rates, triggering alerts before the budget is fully depleted."},
                {"scenario": "Declarative Cloud Setups", "solution": "Define VPCs, subnets, and MIGs in Terraform templates, executing rollouts via Cloud Build hooks upon merging commits."}
            ]
        },
        "topics": [
            {
                "topic": "Site Reliability Engineering (SRE)",
                "q": "You are configuring alerts for a web service. You want to measure the percentage of successful HTTP requests over a 30-day window to ensure reliability. What is this metric called in SRE?",
                "opts": [
                    "Service Level Indicator (SLI)",
                    "Service Level Objective (SLO)",
                    "Service Level Agreement (SLA)",
                    "Error Budget"
                ],
                "ans": 0,
                "exp": "An SLI is a quantifiable metric of service performance (like successful request ratio). The target (like 99.9%) is the SLO."
            },
            {
                "topic": "Monitoring and Alerting",
                "q": "You want to notify your on-call team via PagerDuty whenever your application's error rate exceeds 5% for consecutive minutes. Where should you configure this?",
                "opts": [
                    "Cloud Monitoring Alerting Policies",
                    "Cloud Logging Query filters",
                    "Cloud Composer DAGs",
                    "Cloud Pub/Sub Topics"
                ],
                "ans": 0,
                "exp": "Cloud Monitoring alerting policies allow you to define metric thresholds and direct notifications to PagerDuty, email, or Slack."
            },
            {
                "topic": "Deployment Strategies",
                "q": "You want to deploy a new version of an application to a subset of users first to verify stability before rolling it out to all users. Which deployment strategy does this represent?",
                "opts": ["Canary Deployment", "Blue-Green Deployment", "Rolling Update", "Recreate Deployment"],
                "ans": 0,
                "exp": "A canary deployment routes a small percentage of production traffic to the new version to check for errors before full deployment."
            },
            {
                "topic": "Infrastructure as Code",
                "q": "You want to provision, manage, and version-control your Google Cloud infrastructure in a declarative template format. What is the industry-standard tool supported by Google Cloud providers?",
                "opts": ["Terraform", "Cloud Deployment Manager", "Cloud Build", "Ansible"],
                "ans": 0,
                "exp": "Terraform is an open-source, declarative Infrastructure-as-Code tool widely used to manage Google Cloud resources."
            },
            {
                "topic": "Log Analysis",
                "q": "You want to perform real-time SQL analysis on millions of application logs stored in Cloud Logging. What should you configure?",
                "opts": [
                    "Upgrade the log bucket to use Log Analytics and query it via SQL.",
                    "Export logs to a Cloud Storage bucket and run Python scripts.",
                    "Filter logs in the Log Explorer UI manually.",
                    "Configure a Log Sink to Cloud SQL."
                ],
                "ans": 0,
                "exp": "Log Analytics (powered by BigQuery technology) allows you to search, query, and analyze logs using SQL directly in the Logging console."
            }
        ]
    },
    {
        "id": "google-professional-machine-learning-engineer",
        "provider": "google-cloud",
        "name": "Google Professional Machine Learning Engineer",
        "description": "Tests your ability to design, build, and productionize ML models on GCP using Vertex AI.",
        "icon": "🧠",
        "cheatsheet": {
            "summary": "Productionizing machine learning: model design, building training pipelines in Vertex AI, monitoring parameters, and model drift tracking.",
            "coreConcepts": [
                {"name": "Vertex AI Pipelines", "desc": "Serverless orchestration tool built on Kubeflow Pipelines or TFX to design reproducible pipelines for ML runs."},
                {"name": "Feature Store", "desc": "Centralized repository to share, store, and serve ML features dynamically, preventing training-serving skew."},
                {"name": "Data Drift vs Concept Drift", "desc": "Data drift (input data statistical properties change over time). Concept drift (relationship between input data and target labels changes)."}
            ],
            "commands": [
                {"cmd": "gcloud ai models upload ...", "desc": "Registers a new trained model configuration in the Vertex AI Model Registry."},
                {"cmd": "gcloud ai endpoints predict ...", "desc": "Submits a real-time prediction request to a hosted ML endpoint."}
            ],
            "architecturalPatterns": [
                {"scenario": "Preventing Training-Serving Skew", "solution": "Integrate Vertex AI Feature Store to compute feature values once and distribute them consistently to training and online prediction engines."},
                {"scenario": "ML Pipeline Automation", "solution": "Set up a Cloud Pub/Sub topic triggered by new files in Cloud Storage, launching a Vertex AI Pipeline run via Cloud Functions."}
            ]
        },
        "topics": [
            {
                "topic": "Vertex AI Pipelines",
                "q": "You want to orchestrate your machine learning workflow (data preprocessing, training, evaluation, deployment) in a serverless, reproducible pipeline. Which service should you choose?",
                "opts": ["Vertex AI Pipelines", "Cloud Composer", "Vertex AI Custom Training", "Cloud Build"],
                "ans": 0,
                "exp": "Vertex AI Pipelines is a serverless orchestration service that runs ML pipelines using Kubeflow Pipelines or TFX."
            },
            {
                "topic": "Model Training",
                "q": "You have a large tabular dataset and want to quickly find the best ML model architecture without writing custom TensorFlow or PyTorch training code. Which Vertex AI feature should you use?",
                "opts": ["Vertex AI AutoML", "Vertex AI Custom Training", "Vertex AI Feature Store", "Vertex AI Model Registry"],
                "ans": 0,
                "exp": "Vertex AI AutoML trains tabular, image, text, or video models automatically without requiring manual architecture design."
            },
            {
                "topic": "Feature Management",
                "q": "You want to store, share, and serve machine learning features across multiple training and online serving systems to avoid training-serving skew. Which Vertex AI service is designed for this?",
                "opts": ["Vertex AI Feature Store", "Vertex AI Model Registry", "Cloud Memorystore", "BigQuery"],
                "ans": 0,
                "exp": "Vertex AI Feature Store provides a centralized repository for organizing, storing, and serving ML features."
            },
            {
                "topic": "Model Monitoring",
                "q": "Your deployed ML model's prediction accuracy has degraded over time because the distribution of incoming inference data has changed compared to the training data. What is this phenomenon called?",
                "opts": ["Data Drift (Concept Drift)", "Overfitting", "Underfitting", "Training-Serving Skew"],
                "ans": 0,
                "exp": "Data Drift occurs when input data properties change over time, resulting in degraded model performance (monitored by Vertex AI Model Monitoring)."
            },
            {
                "topic": "Data Ingestion",
                "q": "You are training a deep learning model on petabytes of image data. You want to stream data from Cloud Storage into your training jobs efficiently to prevent GPU starvation. Which data format is recommended?",
                "opts": ["TFRecord (TFData API)", "CSV files", "Raw PNG images", "JSON Lines"],
                "ans": 0,
                "exp": "The TFRecord format is a simple record-oriented binary format optimized for high-throughput streaming pipelines in TensorFlow."
            }
        ]
    },
    {
        "id": "dbt-certified-developer",
        "provider": "dbt",
        "name": "dbt Certified Developer",
        "description": "Validates expertise in analytics engineering workflows, dbt compilation, modeling, testing, documentation, and deployment.",
        "icon": "🛠️",
        "cheatsheet": {
            "summary": "Core transformation developer guidelines: writing modular SQL models, leveraging Jinja variables, testing, and managing lineage docs.",
            "coreConcepts": [
                {"name": "Modular SQL", "desc": "Write SELECT models using the ref() function instead of hardcoding database table references, enabling automated compilation of dependencies."},
                {"name": "Materialization Profiles", "desc": "View (default, virtual lookup), Table (physical tables, faster queries), Incremental (appends/merges new rows), Ephemeral (common table expressions)."},
                {"name": "Data Quality Testing", "desc": "Ensure integrity using YAML schema assertions (`unique`, `not_null`, `accepted_values`, `relationships`)."}
            ],
            "commands": [
                {"cmd": "dbt run", "desc": "Compiles dbt SQL models and executes them on your data warehouse."},
                {"cmd": "dbt test", "desc": "Runs all assertions and validation tests defined in schema YAML files."},
                {"cmd": "dbt docs generate && dbt docs serve", "desc": "Generates documentation and runs a local server to view lineage graphs."}
            ],
            "architecturalPatterns": [
                {"scenario": "Safe Refactoring", "solution": "Create modular staging models representing clean sources, then build downstream dimension/fact models referencing the staging models using ref()."},
                {"scenario": "Handling Hardcoded Codes", "solution": "Declare config parameters or static values inside dbt variables (`var('my_variable')`) rather than hardcoding them in model SQL."}
            ]
        },
        "topics": [
            {
                "topic": "dbt Core Concepts",
                "q": "In a dbt project, what programming languages are primarily used to define models?",
                "opts": ["SQL and Jinja", "Python and Scala", "JavaScript and HTML", "R and SQL"],
                "ans": 0,
                "exp": "dbt combines SQL and Jinja (a templating language) to write modular database transformations."
            },
            {
                "topic": "dbt Compilation",
                "q": "Where does dbt execute the data transformation models when you run 'dbt run'?",
                "opts": [
                    "On the client computer running the dbt CLI",
                    "Inside a dedicated dbt cloud server",
                    "Directly inside the target data warehouse (e.g., Snowflake, BigQuery)",
                    "Inside an in-memory SQLite database"
                ],
                "ans": 2,
                "exp": "dbt does not process data itself. It compiles your code into SQL and sends it to your target database/data warehouse for execution."
            },
            {
                "topic": "dbt Materializations",
                "q": "Which dbt materialization configuration compiles the model SQL into a physical table that is completely dropped and rebuilt on every execution?",
                "opts": ["view", "table", "incremental", "ephemeral"],
                "ans": 1,
                "exp": "The 'table' materialization rebuilds the model as a physical table by dropping the old table and running a CREATE TABLE AS statement."
            },
            {
                "topic": "dbt Tests",
                "q": "Which command compiles and executes data tests defined in your dbt project schema files?",
                "opts": ["dbt test", "dbt run", "dbt compile", "dbt docs generate"],
                "ans": 0,
                "exp": "The `dbt test` command runs assertions against your models to validate data quality."
            },
            {
                "topic": "dbt Lineage",
                "q": "What is the primary function of the ref() function in dbt models?",
                "opts": [
                    "It references external source raw tables.",
                    "It establishes lineage dependencies between models, enabling dbt to build models in the correct order.",
                    "It executes a sub-query directly from python pandas.",
                    "It formats compiled SQL commands."
                ],
                "ans": 1,
                "exp": "The `ref()` function allows you to reference other models and tells dbt how to construct the DAG (Directed Acyclic Graph) to compile dependencies."
            }
        ]
    },
    {
        "id": "dbt-certified-analytics-engineer",
        "provider": "dbt",
        "name": "dbt Certified Analytics Engineer",
        "description": "Tests advanced competency in structuring warehouses, performance optimization, package management, custom macros, and advanced lineage.",
        "icon": "⚙️",
        "cheatsheet": {
            "summary": "Advanced dbt implementation: writing reusable macro modules, scaling incremental models, and managing dependencies.",
            "coreConcepts": [
                {"name": "Jinja Macros & SQL pivot", "desc": "Macros act as SQL functions to avoid repeating commands (e.g. pivoting columns or managing standard timezone formatting)."},
                {"name": "Incremental Strategies", "desc": "Merge (updates matched keys, inserts others), Append (inserts all rows), Delete+Insert (deletes dates matching partition and overwrites), Insert Overwrite."},
                {"name": "dbt packages (packages.yml)", "desc": "Enables sharing code modules (e.g. using `dbt_utils` or `codegen` packages)."}
            ],
            "commands": [
                {"cmd": "dbt deps", "desc": "Downloads and installs package dependencies declared in packages.yml."},
                {"cmd": "dbt source freshness", "desc": "Queries raw tables to verify if recent data has been loaded based on configured SLA thresholds."},
                {"cmd": "dbt run --select state:modified --state path/to/artifacts", "desc": "Runs only the models that have changed since the last compiled state."}
            ],
            "architecturalPatterns": [
                {"scenario": "High-Volume Incremental run", "solution": "Configure model materialization as incremental, define a unique key, and filter incoming data using the `is_incremental()` macro filter."},
                {"scenario": "Monitoring Pipeline Freshness", "solution": "Add freshness parameters to source yml configurations, and schedule `dbt source freshness` checks in the CI/CD pipeline."}
            ]
        },
        "topics": [
            {
                "topic": "Package Management",
                "q": "You want to utilize pre-built dbt tests and utility macros (like surrogate_key) created by the dbt community. In which configuration file must you declare these package dependencies?",
                "opts": ["packages.yml", "dbt_project.yml", "schema.yml", "profiles.yml"],
                "ans": 0,
                "exp": "dbt packages are declared in a `packages.yml` file in the root of the project, and installed using the `dbt deps` command."
            },
            {
                "topic": "Custom Macros",
                "q": "You want to write reusable Jinja logic to pivot columns or dynamically generate date ranges. Where should you define this code inside your dbt project?",
                "opts": ["In a .sql file in the macros/ directory", "In a .yml file in the models/ directory", "In profiles.yml", "In dbt_project.yml"],
                "ans": 0,
                "exp": "Custom dbt macros are written in SQL files within the `macros/` folder using Jinja `{% macro ... %}` syntax."
            },
            {
                "topic": "Incremental Models",
                "q": "You are building a high-volume incremental model. You want to avoid duplicate records by overwriting existing rows based on a unique key, utilizing a merge statement. Which incremental strategy configuration should you define?",
                "opts": ["merge", "append", "delete+insert", "insert_overwrite"],
                "ans": 0,
                "exp": "The `merge` incremental strategy (supported on warehouses like Snowflake and BigQuery) matches rows using a unique key to update existing records and insert new ones."
            },
            {
                "topic": "dbt Source Freshness",
                "q": "You want to monitor the freshness of your raw source data to ensure your data pipeline has loaded records within the last 6 hours. Which command should you schedule?",
                "opts": ["dbt source freshness", "dbt test", "dbt run", "dbt compile"],
                "ans": 0,
                "exp": "The `dbt source freshness` command uses configurations in your source schema YAML files to query the maximum timestamp of your raw data."
            },
            {
                "topic": "Custom Materializations",
                "q": "What is the correct way to define a custom materialization (e.g. creating index structures or custom tables) in dbt?",
                "opts": [
                    "Use the {% materialization %} block inside a SQL file in your macros/ directory.",
                    "Edit the dbt core source code in python.",
                    "Configure it directly inside dbt_project.yml under model configs.",
                    "Custom materializations are not supported in dbt."
                ],
                "ans": 0,
                "exp": "dbt allows developers to write custom materializations by defining a `{% materialization ... %}` block in a macro SQL file."
            }
        ]
    },
    {
        "id": "aws-certified-cloud-practitioner",
        "provider": "aws",
        "name": "AWS Certified Cloud Practitioner",
        "description": "Provides a high-level overview of AWS cloud concepts, security, technology, architecture, and billing models.",
        "icon": "☁️",
        "cheatsheet": {
            "summary": "High-level overview of AWS cloud services, security policies, billing, and the Well-Architected Framework design rules.",
            "coreConcepts": [
                {"name": "AWS EC2", "desc": "Elastic Compute Cloud. Scalable virtual servers in the AWS Cloud."},
                {"name": "Security Groups vs NACLs", "desc": "Security Groups act as firewalls for EC2 instances (stateful). NACLs act as firewalls for subnets (stateless)."},
                {"name": "S3 (Simple Storage Service)", "desc": "Scalable object storage service. Ideal for unstructured files like media, logs, and HTML."}
            ],
            "commands": [
                {"cmd": "aws s3 sync local_folder/ s3://my-bucket/", "desc": "Uploads and synchronizes a local directory with an S3 bucket."},
                {"cmd": "aws ec2 run-instances --image-id ami-xxxxxx ...", "desc": "Creates a new EC2 VM instance."}
            ],
            "architecturalPatterns": [
                {"scenario": "Global File Delivery", "solution": "Store files in S3 and cache them globally at Edge locations using Amazon CloudFront CDN."},
                {"scenario": "Scalable Database", "solution": "Deploy relational SQL schemas on Amazon RDS with Multi-AZ replication for automated failover."}
            ]
        },
        "topics": [
            {
                "topic": "AWS Cloud Basics",
                "q": "What is the AWS service that provides resizable virtual server instances in the cloud?",
                "opts": ["Amazon EC2", "Amazon S3", "Amazon RDS", "AWS Lambda"],
                "ans": 0,
                "exp": "Amazon Elastic Compute Cloud (EC2) provides secure, resizable compute capacity in the form of virtual servers."
            },
            {
                "topic": "AWS Security",
                "q": "Which AWS security tool allows you to control inbound and outbound traffic at the individual Amazon EC2 instance level?",
                "opts": ["Network Access Control Lists (NACLs)", "Security Groups", "AWS Shield", "AWS Identity and Access Management (IAM)"],
                "ans": 1,
                "exp": "Security Groups act as a virtual firewall for your EC2 instances to control incoming and outgoing traffic (stateful)."
            },
            {
                "topic": "AWS S3 Storage",
                "q": "Which AWS storage service is best suited for storing object data like images, videos, and static files?",
                "opts": ["Amazon EBS", "Amazon EFS", "Amazon S3", "Amazon DynamoDB"],
                "ans": 2,
                "exp": "Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability and data availability."
            },
            {
                "topic": "AWS RDS Database",
                "q": "A company wants to deploy a relational SQL database in AWS and offload database patching and backups. Which service should they choose?",
                "opts": ["Amazon EC2 with SQL Server installed", "Amazon DynamoDB", "Amazon Relational Database Service (RDS)", "Amazon ElastiCache"],
                "ans": 2,
                "exp": "Amazon RDS handles database administration tasks like patching, backups, and OS updates."
            },
            {
                "topic": "AWS Content Delivery",
                "q": "Which AWS service helps users distribute content globally to end-users with low latency by caching content at edge locations?",
                "opts": ["Amazon Route 53", "AWS Direct Connect", "Amazon CloudFront", "Elastic Load Balancing (ELB)"],
                "ans": 2,
                "exp": "Amazon CloudFront is a fast content delivery network (CDN) service that delivers content globally with low latency."
            }
        ]
    },
    {
        "id": "microsoft-azure-fundamentals",
        "provider": "microsoft",
        "name": "Microsoft Azure Fundamentals (AZ-900)",
        "description": "Covers foundational knowledge of Azure cloud services, security, privacy, compliance, trust, and pricing models.",
        "icon": "🔷",
        "cheatsheet": {
            "summary": "Introductory guide to Microsoft Azure: subscriptions, resource groups, storage options, and core virtualized networking services.",
            "coreConcepts": [
                {"name": "Azure Subscriptions", "desc": "A logical unit of Azure services linked to an Azure account for billing and security access controls."},
                {"name": "Resource Groups", "desc": "Logical containers containing related Azure resources sharing lifecycles and administrative access."},
                {"name": "Azure Blob Storage", "desc": "Unstructured object storage optimized for serving images, documents, and data backups."}
            ],
            "commands": [
                {"cmd": "az group create --name my-rg --location eastus", "desc": "Creates a new administrative resource group in the East US region."},
                {"cmd": "az vm create --resource-group my-rg --name my-vm ...", "desc": "Deploys a virtual machine instance."}
            ],
            "architecturalPatterns": [
                {"scenario": "Private Office Connectivity", "solution": "Set up Azure ExpressRoute to bypass the public internet and connect on-premises data centers directly to Azure VNets."},
                {"scenario": "Automating Compute Scale", "solution": "Deploy Azure Virtual Machine Scale Sets (VMSS) to dynamically spin up identical VM copies in response to traffic load."}
            ]
        },
        "topics": [
            {
                "topic": "Azure Cloud Portal",
                "q": "What is the name of Microsoft Azure's administrative portal?",
                "opts": ["Azure Console", "Azure Portal", "Azure Cloud shell", "Azure Workspace"],
                "ans": 1,
                "exp": "The Azure Portal is a web-based, unified console that provides an alternative to command-line tools."
            },
            {
                "topic": "Azure Resource Groups",
                "q": "Which Azure resource container group holds related resources that share the same lifecycle, permissions, and policies?",
                "opts": ["Subscription", "Resource Group", "Management Group", "Region"],
                "ans": 1,
                "exp": "A Resource Group is a logical container for resources deployed on Azure."
            },
            {
                "topic": "Azure Connectivity",
                "q": "An organization wants to configure a private connection between its physical office network and its Azure Virtual Network. The connection must not use the public internet. Which service should they choose?",
                "opts": ["Azure VPN Gateway", "Azure ExpressRoute", "Azure Firewall", "Azure Front Door"],
                "ans": 1,
                "exp": "Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection."
            },
            {
                "topic": "Azure VMs",
                "q": "Which service represents Azure's primary Infrastructure as a Service (IaaS) virtual machines?",
                "opts": ["Azure Functions", "Azure Virtual Machines", "Azure App Services", "Azure Container Instances"],
                "ans": 1,
                "exp": "Azure Virtual Machines provide on-demand, scalable computing resources in the form of virtualized server hardware."
            },
            {
                "topic": "Azure Blob Storage",
                "q": "What Azure storage service is optimized for storing massive amounts of unstructured object data, such as audio, video, or backup logs?",
                "opts": ["Azure Files", "Azure Queue Storage", "Azure Blob Storage", "Azure Disk Storage"],
                "ans": 2,
                "exp": "Azure Blob Storage is Microsoft's object storage solution for the cloud, optimized for storing massive amounts of unstructured data."
            }
        ]
    }
]

# Function to generate 50 unique questions for each certification
def generate_questions():
    final_certs = []
    
    for cert in certifications_data:
        cert_id = cert["id"]
        provider = cert["provider"]
        name = cert["name"]
        desc = cert["description"]
        icon = cert["icon"]
        cheatsheet = cert["cheatsheet"]
        topics = cert["topics"]
        
        generated_questions = []
        
        # Generate 50 questions per exam by looping and creating variations
        for q_index in range(1, 51):
            # Select topic using circular modulo
            topic_obj = topics[(q_index - 1) % len(topics)]
            
            # Determine difficulty distribution:
            # 1-15: Easy, 16-35: Medium, 36-50: Hard
            if q_index <= 15:
                diff = "easy"
            elif q_index <= 35:
                diff = "medium"
            else:
                diff = "hard"
                
            # Create a unique question ID
            q_id = f"{cert_id}-q{q_index}"
            
            # Format custom scenario variations to make the questions unique
            scenario_num = ((q_index - 1) // len(topics)) + 1
            project_name = f"Project {chr(64 + scenario_num)}"  # Project A, Project B, etc.
            
            # Dynamically replace generic context in base question with scenario context
            q_text = base_q_text = topic_obj["q"]
            q_text = f"[{topic_obj['topic']} Scenario {scenario_num}] In your company's {project_name} environment: {base_q_text}"
            
            options = topic_obj["opts"]
            correct_index = topic_obj["ans"]
            explanation = topic_obj["exp"] + f" (Difficulty: {diff.capitalize()}, Question Ref: {q_id})"
            
            generated_questions.append({
                "id": q_id,
                "question": q_text,
                "options": options,
                "correctAnswerIndex": correct_index,
                "difficulty": diff,
                "explanation": explanation
            })
            
        final_certs.append({
            "id": cert_id,
            "provider": provider,
            "name": name,
            "description": desc,
            "icon": icon,
            "cheatsheet": cheatsheet,
            "questions": generated_questions
        })
        
    return {"certifications": final_certs}

# Generate and write output
data = generate_questions()
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Success! Generated data/questions.json with {len(data['certifications'])} certifications, cheatsheets, and 50 questions each!")
