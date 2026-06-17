# Detailed Study Guides & Cheat Sheets for 14 Professional Certifications

def get_cheatsheet_for_cert(cert_id):
    cheatsheets = {
        "google-associate-cloud-engineer": {
            "summary": "Essential practical blueprint for setting up, configuring, deploying, monitoring, and securing GCP environments. Focuses on core infrastructure, container hosting, network topology, and security policies.",
            "coreConcepts": [
                {"name": "IAM Hierarchy & Bindings", "desc": "Organization -> Folder -> Project -> Resource. Access is granted via bindings: Member + Role (Primitive, Predefined, Custom) = Access. Principles prioritize least privilege and group-based assignments."},
                {"name": "VPC Global Network", "desc": "VPCs are global resources. Subnets within them are regional. Internal VMs can communicate across regions natively using private IP addresses over Google's backplane without public internet routing."},
                {"name": "Managed Instance Groups (MIGs)", "desc": "Utilizes instance templates to auto-scale VM instances based on CPU/traffic load, perform auto-healing via HTTP health checks, and support rolling updates with zero downtime."},
                {"name": "Cloud Storage Classes", "desc": "Standard (frequent access), Nearline (accessed < once/30 days, backup storage), Coldline (accessed < once/90 days, archive), Archive (accessed < once/365 days, regulatory compliance/DR)."},
                {"name": "Serverless & Compute Options", "desc": "Compute Engine (IaaS VMs), GKE (hybrid/Kubernetes orchestration), App Engine (PaaS runtime web hosting), Cloud Run (serverless containerized app hosting), Cloud Functions (FaaS event-driven)."},
                {"name": "GKE Pods & Services", "desc": "Pods are smallest deployable units. Services define network access: ClusterIP (internal), NodePort (exposes on VM ports), LoadBalancer (provisions External Load Balancer), Ingress (Layer-7 routing)."},
                {"name": "Cloud SQL vs Cloud Spanner", "desc": "Cloud SQL represents regional relational databases (up to 64TB, supports MySQL/Postgres/SQL Server). Cloud Spanner provides globally scale-out relational transactions with strong consistency."},
                {"name": "Operations Suite (Stackdriver)", "desc": "Cloud Logging (aggregates system logs, routes logs via Log Sinks to BigQuery, GCS, or Pub/Sub), Cloud Monitoring (metrics, dashboards, and triggers alerting policies)."}
            ],
            "commands": [
                {"cmd": "gcloud config set project [PROJECT_ID]", "desc": "Configures and locks the active command-line context to the specified project ID."},
                {"cmd": "gcloud compute instances create [VM_NAME] --zone=[ZONE] --machine-type=[TYPE]", "desc": "Provisions a virtual machine instance in Compute Engine with specified configurations."},
                {"cmd": "gcloud container clusters create [CLUSTER] --num-nodes=[N] --zone=[ZONE]", "desc": "Initializes a managed Kubernetes GKE cluster with N nodes per zone."},
                {"cmd": "gsutil mb -c [CLASS] -l [REGION] gs://[BUCKET_NAME]", "desc": "Creates a Cloud Storage bucket using the specified class and geographic region location."},
                {"cmd": "bq query --use_legacy_sql=false '[SQL_STATEMENT]'", "desc": "Runs an analytical query using standard SQL compiler inside BigQuery datasets."}
            ],
            "architecturalPatterns": [
                {"scenario": "Safe Internet Egress for Private VMs", "solution": "Deploy VMs in a private subnet (no external IPs). Route outgoing traffic (e.g. for software updates) through a Cloud Router and Cloud NAT gateway."},
                {"scenario": "Static Asset Hosting with CDN", "solution": "Store static website media in a Cloud Storage bucket with uniform access. Front the bucket with a Global HTTP(S) Load Balancer and enable Cloud CDN for low-latency caching."},
                {"scenario": "Decoupled Web Processing Tier", "solution": "Frontend instances write task payloads to a Pub/Sub queue. An asynchronous backend worker running on Cloud Run consumes the events and writes output to Firestore."}
            ]
        },
        "google-cloud-digital-leader": {
            "summary": "Business-focused blueprint validating foundational cloud concepts, shared responsibility principles, Google Cloud resource hierarchies, and business cases for database, AI, and analytic migrations.",
            "coreConcepts": [
                {"name": "CapEx vs OpEx Shift", "desc": "Moving from Capital Expenditure (upfront investments in physical servers, power, real estate) to Operational Expenditure (pay-as-you-go elastic utility model matching demand)."},
                {"name": "IaaS vs PaaS vs SaaS", "desc": "Infrastructure (Compute Engine, Disks where you manage OS), Platform (App Engine, Cloud Run where Google manages OS/runtimes), Software (Google Workspace/packaged web apps)."},
                {"name": "Shared Responsibility Model", "desc": "Google manages security 'of' the cloud (physical centers, network fibers, hardware virtualizations). The customer manages security 'in' the cloud (IAM controls, database schemas, firewall configurations)."},
                {"name": "GCP Resource Hierarchy", "desc": "Enforces structure: Organization -> Folders -> Projects -> Resources. Inherits permissions down the hierarchy, enabling automated billing and compliance constraints."},
                {"name": "Total Cost of Ownership (TCO)", "desc": "Calculated by comparing cloud operational fees against baseline on-premises expenses (cooling, electricity, physical space, hardware refreshes, network maintenance staffs)."},
                {"name": "Big Data and AI Offerings", "desc": "BigQuery (serverless data warehouse for analytical SQL), Looker (business intelligence visualization dashboards), Vertex AI (unified AI development platform)."},
                {"name": "Cloud Storage & Databases", "desc": "Cloud Storage (object storage), Cloud SQL (managed SQL), Cloud Spanner (global scale relational), Firestore (NoSQL document)."}
            ],
            "commands": [
                {"cmd": "Google Cloud Pricing Calculator", "desc": "Interactive web utility used to estimate monthly infrastructure pricing based on expected usage patterns."},
                {"cmd": "Billing Alerts & Budgets", "desc": "Configure budget targets and email triggers in Billing Console to prevent unexpected cloud invoice spikes."}
            ],
            "architecturalPatterns": [
                {"scenario": "Legacy Physical Server Migration", "solution": "Migrate on-premises Windows/Linux servers directly to Compute Engine VMs (lift-and-shift) to eliminate datacenter maintenance."},
                {"scenario": "Real-time Sales Insights Dashboard", "solution": "Load sales transaction feeds into BigQuery, aggregate metrics using SQL, and build interactive dashboards using Looker for business stakeholders."}
            ]
        },
        "google-generative-ai-leader": {
            "summary": "Strategic overview of Generative AI capabilities, prompt engineering strategies, RAG architecture, responsible AI evaluations, and Vertex AI enterprise application builder tools.",
            "coreConcepts": [
                {"name": "Generative vs Discriminative AI", "desc": "Generative AI produces new data instances (text, images, audio, code) by learning underlying patterns, whereas Discriminative AI classifies inputs or predicts labels."},
                {"name": "Foundation Models & LLMs", "desc": "Massive deep learning neural networks (like Gemini) pre-trained on diverse datasets, capable of reasoning, translation, and adaptation to custom tasks."},
                {"name": "Retrieval-Augmented Generation (RAG)", "desc": "Architectural design that queries external databases or document stores to retrieve context, appending it to the prompt to ground model outputs in factual, real-time data."},
                {"name": "Responsible AI & Ethics", "desc": "Frameworks for safety auditing, fairness, transparency, and bias reduction under Google Cloud's AI Principles. Employs safety filters to block harmful inputs/outputs."},
                {"name": "Prompt Engineering vs Tuning", "desc": "Prompt Engineering designs context within input queries. Tuning (e.g. Fine-Tuning, Parameter-Efficient Tuning) updates actual model weights using training data."},
                {"name": "Vertex AI Agent Builder", "desc": "No-code/low-code platform that lets enterprises build search engines and conversational chatbots grounded in internal PDFs, websites, or database sources."},
                {"name": "Gemini for Google Cloud", "desc": "Always-on AI collaborator providing code suggestions, log analysis, configuration troubleshooting, and billing guidance inside the GCP console."}
            ],
            "commands": [
                {"cmd": "Vertex AI Studio Playground", "desc": "Interactive console for prototyping prompts, configuring temperature parameters, and comparing response outputs."},
                {"cmd": "Agent Builder Grounding Config", "desc": "Bind custom agent instances to secure Google Cloud Storage or BigQuery data stores containing internal wikis."}
            ],
            "architecturalPatterns": [
                {"scenario": "Enterprise Customer Support Bot", "solution": "Create a chat agent using Vertex AI Agent Builder, link it to customer documentation stored in GCS, and embed it as a grounded web assistant."},
                {"scenario": "Secure Regulatory Document Search", "solution": "Establish a search engine grounded in internal financial records inside a VPC Service Controls perimeter. Configure safety thresholds to block sensitive outputs."}
            ]
        },
        "google-professional-cloud-architect": {
            "summary": "Advanced design blueprint for enterprise environments. Focuses on multi-region high availability, compliance guardrails, disaster recovery, global load balancing, and secure hybrid cloud connectivity.",
            "coreConcepts": [
                {"name": "HA & Disaster Recovery (DR)", "desc": "Active-Active configurations distribute request loads. Active-Passive uses failover routes. RTO (recovery speed) and RPO (data loss threshold) dictate storage replication choices."},
                {"name": "GCP Global Load Balancing", "desc": "Global External HTTP(S) LB (Layer-7 routing, SSL offloading, Cloud Armor, and CDN integration). Network Load Balancers (Layer-4 TCP/UDP, high throughput)."},
                {"name": "VPC Service Controls Perimeters", "desc": "Establishes a security perimeter around multi-tenant APIs (like Cloud Storage or BigQuery) to prevent malicious or accidental data exfiltration."},
                {"name": "Enterprise Hybrid Interconnect", "desc": "Dedicated Interconnect (direct physical links to Google cores, 10G/100G, highest SLAs). Partner Interconnect (private links via ISPs). HA VPN (99.99% SLA, IPsec over public web)."},
                {"name": "Governance & Organization Policies", "desc": "Define organizational-level rules (e.g., block external IPs on VMs, restrict locations to US/Europe, enforce Shared VPC structures across folders)."},
                {"name": "Databases at Scale", "desc": "Cloud Spanner (fully managed, relational, synchronous multi-region replication, horizontal scale). Bigtable (low-latency NoSQL time-series). BigQuery (petabyte-scale serverless analytics)."}
            ],
            "commands": [
                {"cmd": "gcloud compute interconnects create ...", "desc": "Initiates configuration of a physical direct fiber connection to Google Cloud network edge."},
                {"cmd": "gcloud compute shared-vpc enable [HOST_PROJECT]", "desc": "Designates the specified project as the host project to share subnets across tenant service projects."},
                {"cmd": "gcloud org-policies set-policy [POLICY_YAML]", "desc": "Applies system-wide organization policies to block insecure defaults (e.g. IAM service account key creations)."}
            ],
            "architecturalPatterns": [
                {"scenario": "Global Relational Web Application", "solution": "Front-end traffic routed via Global HTTP(S) Load Balancer to MIGs in US and Europe. Data tier deployed on a multi-region Cloud Spanner database for global consistency."},
                {"scenario": "Secure Enterprise Data ingestion", "solution": "Ingest database backups from on-premises over Dedicated Interconnect. Process logs in a Project enclosed in a VPC Service Controls perimeter, storing outputs in BigQuery."},
                {"scenario": "Compliance Log Storage", "solution": "Set up an organizational log sink to export all system and access logs into a central bucket configured with Cloud Storage Object Retention Lock."}
            ]
        },
        "google-professional-data-engineer": {
            "summary": "Data architecture blueprint validating pipeline pipelines, streaming analytics (Dataflow/PubSub), serverless warehouses (BigQuery), time-series databases (Bigtable), and compliance orchestrations.",
            "coreConcepts": [
                {"name": "BigQuery Partitioning & Clustering", "desc": "Partitioning splits tables by date or integer range (limits scanned bytes). Clustering sorts data by key columns inside partitions (speeds up grouping/filtering)."},
                {"name": "Cloud Bigtable Row Key Design", "desc": "NoSQL wide-column time-series store. Avoid sequential keys (e.g. timestamp first) to prevent hotspotting. Design row keys as sensor_id#timestamp to group queries."},
                {"name": "Dataflow Windowing & Stream", "desc": "Based on Apache Beam. Tumbling (fixed non-overlapping), Hopping (overlapping), Session (inactivity gap). Watermarks track event-time vs processing-time progression."},
                {"name": "Composer Workflow Orchestration", "desc": "Fully managed Apache Airflow. Runs Directed Acyclic Graphs (DAGs) in Python to automate ETL pipeline steps, coordinate Dataproc Spark jobs, and trigger BigQuery updates."},
                {"name": "Data Security & DLP masking", "desc": "Utilize Cloud Data Loss Prevention (DLP) API to scan, identify, and redact PII data (e.g., credit card numbers, SSNs) inside streaming pipelines before database writes."}
            ],
            "commands": [
                {"cmd": "bq mk --table --expiration 3600 --partition_by date [TABLE]", "desc": "Creates a structured date-partitioned BigQuery table with resource expiration policies."},
                {"cmd": "bq query --use_legacy_sql=false 'SELECT ...'", "desc": "Executes analytical SQL commands against BigQuery datasets using standard SQL engine."},
                {"cmd": "gcloud dataproc clusters create [CLUSTER] --region=[REG] --enable-component-gateway", "desc": "Deploys a managed Apache Spark/Hadoop processing cluster on compute nodes."}
            ],
            "architecturalPatterns": [
                {"scenario": "Real-time Clickstream Analysis", "solution": "Stream web events to Pub/Sub, compute metrics using sliding windows in Dataflow, and stream directly into BigQuery for visualization."},
                {"scenario": "Time-Series IoT Telemetry", "solution": "Ingest millisecond sensor data into Pub/Sub, parse and filter metrics in Dataflow, and write outputs to Bigtable using a row key structure of 'sensor_id#timestamp'."},
                {"scenario": "GDPR Compliant Data Lake", "solution": "Upload files to a staging Cloud Storage bucket. Trigger a Dataflow job that calls the DLP API to mask PII data, and load the anonymized records into BigQuery."}
            ]
        },
        "google-professional-cloud-developer": {
            "summary": "Development blueprint focusing on serverless app design (Cloud Run/Functions), API authentication, CI/CD orchestration, distributed tracing, profiling, and secure configuration management.",
            "coreConcepts": [
                {"name": "Serverless Scaling & Runtimes", "desc": "Cloud Run runs containerized microservices, scaling down to zero when idle. Set minimum instances to prevent cold starts. Adjust concurrency settings to optimize throughput per instance."},
                {"name": "CI/CD & Release Management", "desc": "Automated pipelines: Cloud Build compiles code, Artifact Registry stores images securely, and Cloud Deploy coordinates canary or blue-green releases to GKE or Cloud Run."},
                {"name": "Distributed Trace & Monitoring", "desc": "Cloud Trace logs HTTP request latencies across microservice boundaries. Cloud Profiler monitors CPU and memory usage in code. Cloud Logging captures console outputs."},
                {"name": "API Gateways & Security", "desc": "Expose microservices using API Gateway or Apigee for request throttling, API key verification, OAuth authentication, and cataloging REST resources."},
                {"name": "Secrets Management", "desc": "Store sensitive keys (API tokens, passwords) in Secret Manager. Grant the compute service account Secret Manager Viewer access, and inject secrets as env variables at startup."}
            ],
            "commands": [
                {"cmd": "gcloud builds submit --config=cloudbuild.yaml --substitutions=_IMAGE=[IMG]", "desc": "Triggers a build on Cloud Build and substitutes variables dynamically."},
                {"cmd": "gcloud secrets versions access latest --secret=[NAME]", "desc": "Reads the raw payload of the latest active secret version from the command-line."},
                {"cmd": "gcloud run deploy [SERVICE] --image=[IMG] --concurrency=[N] --min-instances=[M]", "desc": "Deploys service to Cloud Run with customized scaling and concurrency configurations."}
            ],
            "architecturalPatterns": [
                {"scenario": "Serverless API Backend with Caching", "solution": "Deploy a Node.js microservice to Cloud Run. Cache frequent database query outputs in Cloud Memorystore (Redis) to decrease response latencies."},
                {"scenario": "Decoupled Asynchronous Transaction Pipeline", "solution": "Submit transactions to API Gateway. Write records to Pub/Sub to decouple services, and process transactions asynchronously via a worker container on Cloud Run."}
            ]
        },
        "google-professional-cloud-security-engineer": {
            "summary": "Advanced security blueprint covering key management (KMS), resource perimeters (VPC SC), firewall structures, WAF filtering (Cloud Armor), identity proxies (IAP), and sensitive data management.",
            "coreConcepts": [
                {"name": "Encryption at Rest Portfolio", "desc": "GMEK (Google-Managed, default), CMEK (Customer-Managed, key generation/lifecycle in Cloud KMS), CSEK (Customer-Supplied, keys managed on-premises)."},
                {"name": "VPC Service Controls", "desc": "Locks down APIs (like GCS or BigQuery) by enclosing projects in service perimeters, preventing network exfiltrations and restricting traffic to verified sources."},
                {"name": "Identity-Aware Proxy (IAP)", "desc": "Secures web applications running on App Engine, GKE, or VMs without using VPNs, by verifying user identity and context via IAM policy rules."},
                {"name": "Cloud Armor & WAF", "desc": "Provides Layer-7 firewall filtering, DDoS mitigation, and OWASP Top 10 web attack protection (e.g. blocking SQL injections) at HTTP(S) Load Balancer level."},
                {"name": "IAM Governance & Workload Identity", "desc": "Workload Identity allows GKE Pods to authenticate directly as GCP Service Accounts, avoiding the need to download or mount static private service account key files."}
            ],
            "commands": [
                {"cmd": "gcloud kms keyrings create [RING] --location=[LOC]", "desc": "Initializes a key vault keyring wrapper at a specific location."},
                {"cmd": "gcloud kms keys create [KEY] --keyring=[RING] --purpose=encryption", "desc": "Generates a key within the keyring for data encryption purposes."},
                {"cmd": "gcloud compute firewall-rules create [RULE] --allow=tcp:22 --source-ranges=35.235.240.0/20", "desc": "Creates a firewall rule to allow SSH access only via Cloud IAP TCP forwarding range."}
            ],
            "architecturalPatterns": [
                {"scenario": "Zero-Trust Web Portal access", "solution": "Expose an internal administrative portal running on Compute Engine VMs behind an HTTPS Load Balancer with Identity-Aware Proxy (IAP) enabled, restricting access to verified company users."},
                {"scenario": "Secure BigQuery Processing", "solution": "Isolate the BigQuery database and raw data storage buckets inside a VPC Service Controls perimeter. Configure an ingress rule to allow access only from an authorized VPC network."},
                {"scenario": "PII Data Auditing", "solution": "Stream logs to a Pub/Sub topic, execute a Dataflow pipeline that calls the DLP API to mask SSNs and phone numbers, and save the sanitized logs to BigQuery."}
            ]
        },
        "google-professional-cloud-network-engineer": {
            "summary": "Advanced network engineering blueprint. Focuses on VPC architectures, Shared VPC design, hybrid routes (Interconnect/VPN), BGP configurations, private endpoint resolutions, and CDN caching.",
            "coreConcepts": [
                {"name": "Shared VPC Architecture", "desc": "Shares VPC subnets from a central Host Project to multiple Service Projects, enforcing administrative network segregation while enabling shared compute connectivity."},
                {"name": "VPC Network Peering", "desc": "Connects two VPC networks internally with low latency and high bandwidth across distinct organizations, without using public gateway hops."},
                {"name": "Hybrid Connectivities", "desc": "Dedicated Interconnect (direct physical fiber, 10G/100G). Partner Interconnect (private ISP circuit, 50M-10G). HA VPN (99.99% SLA, IPsec over public web, dual tunnels)."},
                {"name": "Dynamic Routing with BGP", "desc": "Uses Cloud Router to exchange routing tables dynamically using Border Gateway Protocol (BGP) over VPN or Interconnect links to on-premises routers."},
                {"name": "Private Google Access", "desc": "Enables VM instances that only have internal IP addresses in a subnet to reach global Google APIs (like BigQuery, GCS) securely without public internet routes."}
            ],
            "commands": [
                {"cmd": "gcloud compute networks create [NAME] --subnet-mode=custom", "desc": "Creates a custom-mode VPC network without auto-generated default regional subnets."},
                {"cmd": "gcloud compute networks subnets create [SUBNET] --network=[NET] --range=10.1.0.0/24 --enable-private-ip-google-access", "desc": "Creates a subnet and enables Private Google Access."},
                {"cmd": "gcloud compute routers create [ROUTER] --network=[NET] --asn=65001", "desc": "Deploys a Cloud Router with a BGP Autonomous System Number (ASN)."}
            ],
            "architecturalPatterns": [
                {"scenario": "Enterprise Shared Network Infrastructure", "solution": "Deploy all subnets, firewalls, and Interconnect lines in a Shared VPC host project. Share subnets with application-specific service projects for isolation."},
                {"scenario": "Cross-Cloud Network Resolution", "solution": "Establish a VPN tunnel to AWS. Configure Cloud DNS forwarding zones in GCP to route requests for '.aws' domains to AWS Route53 resolvers."}
            ]
        },
        "google-professional-cloud-devops-engineer": {
            "summary": "DevOps and SRE blueprint validating deployment automations, CI/CD canary strategies, SLI/SLO metric configurations, error budget management, logging routers, and IaC provisioning.",
            "coreConcepts": [
                {"name": "SLIs, SLOs, and SLAs", "desc": "SLI (Service Level Indicator, e.g. latency). SLO (Service Level Objective, e.g. latency < 200ms for 99.9% of calls). SLA (Service Level Agreement, legal contract with penalties)."},
                {"name": "Error Budget Management", "desc": "The acceptable level of failure (100% - SLO). Used to balance feature deployment speed against system stability. Budget depletion pauses deployments."},
                {"name": "Canary & Blue-Green Releases", "desc": "Canary rolls out updates to a small subset of servers or users first. Blue-Green switches traffic instantly from green (old) to blue (new) target groups."},
                {"name": "Infrastructure as Code (IaC)", "desc": "Using Terraform to define, version, and provision GCP infrastructure. Prevents configuration drift and automates environment setups."},
                {"name": "Logging Routers & Sinks", "desc": "Routes logs from projects, folders, or organizations to BigQuery for SQL analysis, Pub/Sub for real-time alerting, or GCS for long-term audit storage."}
            ],
            "commands": [
                {"cmd": "terraform init && terraform apply -auto-approve", "desc": "Initializes and provisions declared resources using local state configurations."},
                {"cmd": "gcloud deploy releases create [RELEASE] --delivery-pipeline=[PIPELINE] --source=[PATH]", "desc": "Initiates a release deployment process using Cloud Deploy delivery configurations."},
                {"cmd": "gcloud logging sinks create [SINK_NAME] bigquery.googleapis.com/projects/[PROJ]/datasets/[DATASET] --log-filter='severity>=ERROR'", "desc": "Creates a Log Sink to export error logs to BigQuery."}
            ],
            "architecturalPatterns": [
                {"scenario": "Automated Canary Deployments", "solution": "Configure Cloud Deploy targeting GKE. Deploy code to 10% target. Monitor SLIs/SLOs in Cloud Monitoring. Auto-promote to 100% if SLOs remain intact."},
                {"scenario": "Auditable Infrastructure Pipeline", "solution": "Manage resources in Git. A merge to main triggers Cloud Build to run Terraform plan, output audits to Cloud Logging, and execute terraform apply."}
            ]
        },
        "google-professional-machine-learning-engineer": {
            "summary": "ML engineering blueprint focusing on model design, distributed training, pipeline integrations (Vertex AI), prediction endpoints, MLOps, and model drift tracking.",
            "coreConcepts": [
                {"name": "Vertex AI Pipelines & SDK", "desc": "Coordinates ML workflows using Kubeflow Pipelines (KFP) or TensorFlow Extended (TFX) to orchestrate data loading, training, and evaluations."},
                {"name": "Model Training Architectures", "desc": "Custom containers run custom model code. Distributed training scales across multiple compute instances using GPUs or Tensor Processing Units (TPUs)."},
                {"name": "Model Deployments & Serving", "desc": "Deploys model files to Vertex AI Endpoints for low-latency online predictions, or triggers Batch Prediction jobs for processing high-volume datasets."},
                {"name": "MLOps, Skew, and Drift Monitoring", "desc": "Skew is the difference between training and serving data distributions. Drift is the change in serving data distributions over time. Vertex AI monitors both."},
                {"name": "Feature Store Management", "desc": "Vertex AI Feature Store provides a centralized repository to store, share, and serve machine learning features, ensuring feature consistency between training and online serving."}
            ],
            "commands": [
                {"cmd": "gcloud ai custom-jobs create --display-name=[NAME] --config=config.yaml", "desc": "Submits a custom model training container job to Vertex AI."},
                {"cmd": "gcloud ai endpoints predict [ENDPOINT] --json-request=inputs.json", "desc": "Sends live feature inputs to a deployed Vertex AI model endpoint for online predictions."}
            ],
            "architecturalPatterns": [
                {"scenario": "Automated Model Training Pipeline", "solution": "Run a daily pipeline in Vertex AI Pipelines that extracts transactional data from BigQuery, processes features, trains an XGBoost model, and registers it in the Model Registry."},
                {"scenario": "Production Model Drift Alerts", "solution": "Deploy model to an Endpoint. Configure Vertex AI Model Monitoring to sample live inference traffic and send email alerts if feature drift thresholds are breached."}
            ]
        },
        "dbt-certified-analytics-engineer": {
            "summary": "Analytics engineering study guide focusing on SQL modeling, Jinja macro structures, model materializations, dependencies (ref/source), test configurations, and slowly changing dimensions (Snapshots).",
            "coreConcepts": [
                {"name": "dbt Project Structure", "desc": "Configured in 'dbt_project.yml'. Main directories: models/ (SQL files), seeds/ (small static CSVs), macros/ (reusable Jinja functions), analyses/ (one-off SQL)."},
                {"name": "dbt Materialization Types", "desc": "View (default, virtual table), Table (re-built on each run), Incremental (appends new records based on filters), Ephemeral (nested as inline CTEs)."},
                {"name": "Refs & Sources (DAG Building)", "desc": "The ref() function links models, building the Directed Acyclic Graph (DAG) for dependencies. The source() function references raw source tables in the data warehouse."},
                {"name": "Testing (Schema vs Data)", "desc": "Schema tests validate constraints (unique, not_null, accepted_values, relationships) inside YAML files. Data tests are custom SQL files that return failing rows."},
                {"name": "dbt Seeds vs Snapshots", "desc": "Seeds are static lookup tables compiled from CSV files. Snapshots capture change history over time, implementing SCD Type 2 columns (valid_from, valid_to)."}
            ],
            "commands": [
                {"cmd": "dbt run", "desc": "Compiles dbt models into raw SQL and executes them, materializing tables/views in the target data warehouse."},
                {"cmd": "dbt test", "desc": "Runs all configured tests against materialized database tables, outputting failures in the console."},
                {"cmd": "dbt compile", "desc": "Translates dbt Jinja SQL files into raw SQL code, locating outputs in the target/ folder without executing them."},
                {"cmd": "dbt docs generate && dbt docs serve", "desc": "Builds documentation JSON files from project yml descriptions and launches a local documentation server."},
                {"cmd": "dbt run --select [MODEL_NAME]+", "desc": "Runs the specified model and all of its downstream dependencies."}
            ],
            "architecturalPatterns": [
                {"scenario": "Warehouse Data Mart Modeling", "solution": "Ingest raw transaction logs. Build staging models (data type casting), intermediate models (aggregating dimensions), and final mart tables for BI tools."},
                {"scenario": "Incremental High-Volume Log Loading", "solution": "Configure a model with incremental materialization. Use Jinja block 'is_incremental()' to load only rows newer than the max active date in the target table."}
            ]
        },
        "dbt-certified-developer": {
            "summary": "Advanced software engineering practices with dbt. Covers dynamic Jinja scripting, packages manager, CI/CD slim runs, custom schema architectures, and metadata queries.",
            "coreConcepts": [
                {"name": "Advanced Jinja & Adapter Macros", "desc": "Using Jinja control flow and loop structures. Utilizing adapter methods like 'adapter.dispatch()' to run distinct SQL based on database engine."},
                {"name": "dbt Package Management", "desc": "Imports open-source packages (e.g., dbt_utils) by declaring dependencies in 'packages.yml' and running install commands to import macros."},
                {"name": "Slim CI/CD Deployments", "desc": "dbt Cloud CI runs only compile and test modified models and their downstream dependencies using 'state:modified+' options, saving warehouse compute costs."},
                {"name": "Custom Schema Configurations", "desc": "Override default schema placements. Configure 'generate_schema_name' macro to route staging models to dev schemas and marts to production schemas."},
                {"name": "Artifacts & Metadata APIs", "desc": "dbt runs compile files like 'manifest.json' and 'run_results.json'. These artifacts can be parsed to audit execution times and model dependencies."}
            ],
            "commands": [
                {"cmd": "dbt deps", "desc": "Downloads and installs external dbt packages configured in packages.yml."},
                {"cmd": "dbt debug", "desc": "Validates database connection credentials, profiles file paths, and local project configuration variables."},
                {"cmd": "dbt run --select state:modified+ --defer --state path/to/artifacts", "desc": "Runs only modified models and downstream dependencies in CI, deferring unchanged tables to production schemas."}
            ],
            "architecturalPatterns": [
                {"scenario": "Warehouse-Agnostic Date Math Macro", "solution": "Create a macro that uses 'adapter.dispatch()'. Define different SQL syntaxes for BigQuery and Snowflake to handle date calculations dynamically."},
                {"scenario": "Automated Slim CI PR Checks", "solution": "Integrate GitHub Actions with dbt Cloud. A PR run compiles only changed code, deferring to the production manifest to run slim CI checks."}
            ]
        },
        "aws-certified-cloud-practitioner": {
            "summary": "Foundational AWS credentials validating core global infrastructure, compute, storage, databases, IAM security models, billing features, and pricing structures.",
            "coreConcepts": [
                {"name": "AWS Global Infrastructure", "desc": "Regions (geographical clusters of AZs), Availability Zones (AZs, isolated datacenters), Edge Locations (caching destinations for CloudFront CDN)."},
                {"name": "Compute Services Portfolio", "desc": "Amazon EC2 (IaaS VMs), AWS Lambda (serverless event-driven functions), Amazon ECS/EKS (managed container platforms)."},
                {"name": "Storage Services Portfolio", "desc": "Amazon S3 (object storage), Amazon EBS (block storage volumes for EC2), Amazon EFS (managed shared network file systems)."},
                {"name": "Databases Portfolio", "desc": "Amazon RDS (managed relational DB), Amazon DynamoDB (serverless NoSQL document DB), Amazon Aurora (high-performance relational DB)."},
                {"name": "AWS Shared Responsibility Model", "desc": "AWS manages security 'of' the cloud (datacenter infrastructure). The customer manages security 'in' the cloud (data configurations, IAM users, firewall groups)."},
                {"name": "AWS IAM Identity Management", "desc": "AWS Identity and Access Management. Controls user logins, policies, and permissions. Enforces multi-factor authentication (MFA)."},
                {"name": "Billing & Budgeting Tools", "desc": "AWS Billing Dashboard, AWS Budgets (configures spend alert thresholds), AWS Cost Explorer (analyzes historical usage trends)."}
            ],
            "commands": [
                {"cmd": "aws configure", "desc": "Prompts to configure AWS CLI access credentials, default region, and output formatting."},
                {"cmd": "aws s3 mb s3://[BUCKET_NAME]", "desc": "Creates a new Amazon S3 bucket globally."},
                {"cmd": "aws ec2 run-instances --image-id ami-xxxxxx --instance-type t3.micro", "desc": "Launches a basic EC2 instance in the configured subnet."}
            ],
            "architecturalPatterns": [
                {"scenario": "Highly Available AWS Web Application", "solution": "Deploy an Application Load Balancer to distribute traffic to EC2 instances across multiple Availability Zones, backed by an RDS Multi-AZ database."},
                {"scenario": "Global Low-Latency Static Site", "solution": "Store static website files in an S3 bucket. Front the bucket with Amazon CloudFront CDN to cache content globally at edge locations."}
            ]
        },
        "microsoft-azure-fundamentals": {
            "summary": "Foundational Azure credentials validating core geography, compute structures, Blob storage, Microsoft Entra ID authentication, subscription controls, and resource locks.",
            "coreConcepts": [
                {"name": "Azure Core Geographies", "desc": "Azure Regions (geographical areas), Availability Zones (isolated datacenters within a region), Region Pairs (cross-region replication pairs for DR)."},
                {"name": "Compute & Web Resources", "desc": "Azure Virtual Machines (VMs), Azure App Services (PaaS web apps), Azure Kubernetes Service (AKS), Azure Virtual Desktop."},
                {"name": "Blob & Storage Portfolio", "desc": "Azure Blob Storage (unstructured object storage), Azure Files (managed network file shares), Azure Disk Storage (block storage for VMs)."},
                {"name": "Microsoft Entra ID Security", "desc": "Provides identity access management (formerly Azure Active Directory), Role-Based Access Control (RBAC), MFA, and Conditional Access policies."},
                {"name": "Azure Governance & Resource Locks", "desc": "Azure Policies enforce configuration standards. Resource Locks (CannotDelete, ReadOnly) prevent accidental deletions of critical database resource groups."},
                {"name": "Management & Architecture Tools", "desc": "Azure Portal, Azure CLI, Azure Cloud Shell, Azure Resource Manager (ARM templates define declarative infrastructure deployments)."}
            ],
            "commands": [
                {"cmd": "az login", "desc": "Launches a browser session to authenticate and log in the active Azure CLI session."},
                {"cmd": "az group create --name [RG_NAME] --location eastus", "desc": "Initializes a logical resource group container in the specified location."},
                {"cmd": "az vm create --resource-group [RG_NAME] --name [VM_NAME] --image Ubuntu2204", "desc": "Provisions a virtual machine inside the resource group."}
            ],
            "architecturalPatterns": [
                {"scenario": "Automated Infrastructure Deployment", "solution": "Declare Virtual Networks, Subnets, and SQL Databases inside an ARM or Bicep template to guarantee consistent deployments across Dev/Prod environments."},
                {"scenario": "Secured Web Identity Architecture", "solution": "Register a PaaS App Service in Microsoft Entra ID. Assign an RBAC Reader role to the service account, and enforce Conditional Access MFA rules."}
            ]
        }
    }
    return cheatsheets.get(cert_id, {
        "summary": "No study guide cheatsheet configured.",
        "coreConcepts": [],
        "commands": [],
        "architecturalPatterns": []
    })
