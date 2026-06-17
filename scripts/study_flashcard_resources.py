# Study Flashcard Resources - Quick-recall Q&A style flashcards
# These are DIFFERENT from the Exam Guide Checklist (flashcard_resources.py)
# These cover key definitions, numbers, CLI commands, comparisons, and exam gotchas

dbt_cards = [
    {
        "category": "Core Concepts",
        "front": "What is dbt and what does it do?",
        "back": "- dbt (data build tool): SQL-based transformation framework\n- Transforms raw data in the warehouse (ELT, not ETL)\n- Models are SELECT statements that dbt materializes\n- Supports: Snowflake, BigQuery, Redshift, Databricks, PostgreSQL\n- Enables version control, testing, and documentation for analytics"
    },
    {
        "category": "Core Concepts",
        "front": "dbt model materializations?",
        "back": "- table: DROP + CREATE TABLE AS (full refresh)\n- view: CREATE VIEW AS (computed on query)\n- incremental: INSERT/MERGE only new or changed rows\n- ephemeral: CTE inlined into downstream models (not materialized)\n- Use table for small static data, incremental for large datasets\n- Use view for lightweight transformations"
    },
    {
        "category": "Models",
        "front": "ref() vs source() functions?",
        "back": "- ref('model_name'): Reference another dbt model\n- source('source_name', 'table_name'): Reference raw source tables\n- ref() creates a DAG dependency between models\n- source() integrates with source freshness tests\n- Always use ref() to reference other models, never hardcode table names\n- Both handle schema/database resolution automatically"
    },
    {
        "category": "Testing",
        "front": "dbt testing: Schema vs Data tests?",
        "back": "- Schema tests: Defined in YAML (unique, not_null, accepted_values, relationships)\n- Data tests: Custom SQL queries in tests/ directory\n- Generic tests: Reusable test macros with parameters\n- Tests run with 'dbt test' command\n- Failed tests return rows that violate the assertion\n- Severity: warn or error (configurable per test)"
    },
    {
        "category": "Sources",
        "front": "Source freshness monitoring?",
        "back": "- Defined in YAML with loaded_at_field and freshness thresholds\n- warn_after and error_after with count and period\n- Run with 'dbt source freshness' command\n- Checks if source data is stale based on loaded_at column\n- Integrates with CI/CD to alert on data pipeline issues\n- Results stored in target/sources.json"
    },
    {
        "category": "Macros",
        "front": "Jinja and macros in dbt?",
        "back": "- Jinja: Templating language for dynamic SQL\n- {{ }} for expressions, {% %} for statements, {# #} for comments\n- Macros: Reusable Jinja functions defined in macros/ directory\n- Built-in macros: date_spine, generate_schema_name, etc.\n- dbt_utils package: Common utility macros\n- Use macros to DRY up repetitive SQL patterns"
    },
    {
        "category": "Documentation",
        "front": "dbt documentation features?",
        "back": "- Describe models, columns, and tests in YAML files\n- doc blocks: Markdown documentation in .md files\n- 'dbt docs generate' creates documentation site\n- 'dbt docs serve' hosts documentation locally\n- Auto-generated lineage graph (DAG visualization)\n- Column-level descriptions show in data catalog tools"
    },
    {
        "category": "Packages",
        "front": "dbt packages and packages.yml?",
        "back": "- External reusable dbt code (models, macros, tests)\n- Defined in packages.yml at project root\n- Install with 'dbt deps' command\n- Popular: dbt_utils, dbt_expectations, codegen\n- Hub packages from hub.getdbt.com\n- Git packages from private or public repositories"
    },
    {
        "category": "Incremental",
        "front": "Incremental model strategies?",
        "back": "- append: INSERT new rows only (fastest, no updates)\n- merge: MERGE/upsert based on unique_key (handles updates)\n- delete+insert: Delete matching rows, then insert\n- insert_overwrite: Replace entire partitions\n- is_incremental() macro: Differentiate full vs incremental runs\n- --full-refresh flag forces complete rebuild"
    },
    {
        "category": "Project Structure",
        "front": "dbt project structure best practices?",
        "back": "- staging/: 1:1 with source tables, light transformations\n- intermediate/: Business logic joins and aggregations\n- marts/: Final business entities for consumers\n- sources.yml: Source definitions with freshness and tests\n- schema.yml: Model and column descriptions and tests\n- Naming: stg_source__table, int_subject__verb, fct/dim_entity"
    },
    {
        "category": "Snapshots",
        "front": "dbt snapshots: SCD Type 2?",
        "back": "- Track historical changes in source data (Slowly Changing Dimensions)\n- strategy: timestamp or check\n- timestamp: Uses updated_at column to detect changes\n- check: Compares column values for changes\n- Adds dbt_valid_from, dbt_valid_to, dbt_scd_id columns\n- Run with 'dbt snapshot', defined in snapshots/ directory"
    },
    {
        "category": "Seeds",
        "front": "dbt seeds: What and when?",
        "back": "- CSV files stored in the seeds/ directory of your project\n- Load into warehouse with 'dbt seed' command\n- Use for small, static reference data (country codes, mappings)\n- NOT for large datasets (use sources instead)\n- Can override column types in dbt_project.yml\n- Version-controlled with your dbt project"
    },
    {
        "category": "CLI",
        "front": "Essential dbt CLI commands?",
        "back": "- dbt run: Execute all models\n- dbt test: Run all tests\n- dbt build: Run + test in DAG order\n- dbt compile: Generate SQL without executing\n- dbt deps: Install packages from packages.yml\n- dbt run --select model_name: Run specific model\n- dbt run --select tag:daily: Run models with tag"
    },
    {
        "category": "Advanced",
        "front": "dbt hooks and operations?",
        "back": "- pre-hook: SQL executed before a model runs\n- post-hook: SQL executed after a model runs\n- on-run-start: SQL at beginning of dbt run\n- on-run-end: SQL at end of dbt run\n- Use for: GRANT permissions, ANALYZE tables, custom logging\n- Defined in dbt_project.yml or model config blocks"
    },
    {
        "category": "Advanced",
        "front": "dbt exposures and metrics?",
        "back": "- Exposures: Document downstream consumers (dashboards, ML models)\n- Define in YAML with type, owner, depends_on\n- Shows in DAG which models feed which business tools\n- Metrics: Define business metrics in YAML (deprecated in favor of Semantic Layer)\n- dbt Semantic Layer: Centralized metric definitions for BI tools\n- Ensures consistent metric calculations across the organization"
    }
]

def get_study_flashcards_for_cert(cert_id):
    flashcards = {
        "google-associate-cloud-engineer": [
            {
                "category": "Compute",
                "front": "What is the difference between Compute Engine and App Engine?",
                "back": "- Compute Engine = IaaS (you manage VMs, OS, patches)\n- App Engine = PaaS (Google manages infrastructure)\n- App Engine Standard: auto-scales to zero, limited runtimes\n- App Engine Flexible: runs custom Docker containers, minimum 1 instance"
            },
            {
                "category": "Compute",
                "front": "What is Cloud Run?",
                "back": "- Fully managed serverless container platform\n- Scales to zero (no charge when idle)\n- Supports any language/binary via containers\n- Max request timeout: 60 minutes\n- Pay per 100ms of CPU/memory used"
            },
            {
                "category": "Compute",
                "front": "What is a Managed Instance Group (MIG)?",
                "back": "- Group of identical VMs created from an instance template\n- Supports autoscaling based on CPU, HTTP load, or custom metrics\n- Auto-healing via health checks\n- Rolling updates and canary deployments\n- Regional MIGs span multiple zones for HA"
            },
            {
                "category": "Compute",
                "front": "Preemptible VMs vs Spot VMs?",
                "back": "- Both are up to 60-91% cheaper than regular VMs\n- Preemptible: max 24-hour lifetime, can be reclaimed anytime\n- Spot VMs: same pricing, no max lifetime limit\n- Both ideal for batch processing, fault-tolerant workloads\n- No SLA, no live migration"
            },
            {
                "category": "Storage",
                "front": "Cloud Storage classes and minimum storage durations?",
                "back": "- Standard: No minimum duration, frequent access\n- Nearline: 30-day minimum, accessed < once/month\n- Coldline: 90-day minimum, accessed < once/quarter\n- Archive: 365-day minimum, accessed < once/year\n- All classes have the same API and millisecond access time"
            },
            {
                "category": "Storage",
                "front": "Cloud SQL vs Cloud Spanner vs Firestore?",
                "back": "- Cloud SQL: Regional relational DB (MySQL, PostgreSQL, SQL Server), max 64TB, vertical scaling\n- Cloud Spanner: Global relational DB with horizontal scaling, strong consistency, 99.999% SLA\n- Firestore: Serverless NoSQL document DB, real-time sync, offline support\n- Use Cloud SQL for traditional apps, Spanner for global scale, Firestore for mobile/web"
            },
            {
                "category": "Networking",
                "front": "What is a VPC and how are subnets scoped?",
                "back": "- VPC = Virtual Private Cloud, a global resource\n- Subnets are regional (span all zones in a region)\n- VMs in different regions of same VPC communicate via internal IPs\n- Default VPC created with auto-mode subnets in each region\n- Custom mode VPCs give full control over IP ranges"
            },
            {
                "category": "Networking",
                "front": "Firewall rules priority and defaults?",
                "back": "- Priority range: 0 (highest) to 65535 (lowest)\n- Default rules: deny all ingress (priority 65535), allow all egress (priority 65535)\n- Implied rules cannot be deleted\n- Rules can target instances by service account or network tag\n- Firewall rules are stateful (return traffic auto-allowed)"
            },
            {
                "category": "IAM",
                "front": "What are the three types of IAM roles?",
                "back": "- Basic (Primitive): Owner, Editor, Viewer - broad permissions, avoid in production\n- Predefined: Fine-grained roles for specific services (e.g., roles/storage.objectViewer)\n- Custom: User-defined roles with specific permissions you select\n- Best practice: Use predefined roles, apply least privilege"
            },
            {
                "category": "IAM",
                "front": "What is a Service Account and how is it used?",
                "back": "- An identity for applications/VMs (not humans)\n- Has an email format: SA_NAME@PROJECT_ID.iam.gserviceaccount.com\n- Attach to VMs/Cloud Run to grant API access\n- Can generate keys (avoid when possible, use attached SAs instead)\n- Default SA has Editor role - too broad, create custom SAs"
            },
            {
                "category": "IAM",
                "front": "IAM resource hierarchy and policy inheritance?",
                "back": "- Hierarchy: Organization → Folder → Project → Resource\n- Policies are inherited downward (union of all policies)\n- Cannot restrict permissions granted at a higher level\n- Organization policies can enforce constraints across all projects\n- Projects are the fundamental billing and resource boundary"
            },
            {
                "category": "Kubernetes",
                "front": "GKE cluster types: Zonal vs Regional?",
                "back": "- Zonal cluster: Single control plane in one zone, nodes in same zone\n- Multi-zonal: Single control plane, nodes across multiple zones\n- Regional: Control plane replicated across 3 zones, nodes across zones\n- Regional clusters provide HA for both control plane and workloads\n- Autopilot mode: Google manages nodes, pay per pod"
            },
            {
                "category": "Kubernetes",
                "front": "GKE Service types for exposing workloads?",
                "back": "- ClusterIP: Internal only (default)\n- NodePort: Exposes on each node's IP at a static port (30000-32767)\n- LoadBalancer: Provisions an external Network Load Balancer\n- Ingress: Layer 7 HTTP(S) load balancer with URL-based routing\n- Use Ingress for production web apps, LoadBalancer for TCP/UDP"
            },
            {
                "category": "Operations",
                "front": "Cloud Logging: Log sinks and export destinations?",
                "back": "- Log sinks filter and route logs to destinations\n- Destinations: Cloud Storage (archival), BigQuery (analysis), Pub/Sub (streaming), Log Buckets\n- Inclusion filters select which logs to export\n- Exclusion filters prevent specific logs from being ingested\n- Admin Activity logs are always on, cannot be disabled"
            },
            {
                "category": "Operations",
                "front": "Cloud Monitoring: Alerting policy components?",
                "back": "- Condition: What metric threshold triggers the alert\n- Notification channel: Email, SMS, Slack, PagerDuty, webhook\n- Documentation: Runbook/notes attached to incident\n- Uptime checks: HTTP(S), TCP, or ICMP probes from global locations\n- Custom metrics can be created via API or OpenTelemetry"
            },
            {
                "category": "CLI",
                "front": "Essential gcloud commands for the ACE exam?",
                "back": "- gcloud config set project PROJECT_ID (set active project)\n- gcloud compute instances create NAME --zone=ZONE\n- gcloud container clusters get-credentials CLUSTER\n- gcloud app deploy (deploy App Engine app)\n- gcloud run deploy --image=IMAGE --platform=managed\n- gsutil mb gs://BUCKET (create Cloud Storage bucket)"
            },
            {
                "category": "Billing",
                "front": "GCP billing concepts and budgets?",
                "back": "- Billing account linked to one or more projects\n- Budgets send alerts at thresholds (50%, 90%, 100%)\n- Budgets do NOT stop spending by default\n- Use billing export to BigQuery for cost analysis\n- Committed Use Discounts (CUDs): 1-3 year for up to 57% off\n- Sustained Use Discounts (SUDs): Auto-applied for consistent usage"
            },
            {
                "category": "Networking",
                "front": "Cloud NAT vs Cloud VPN vs Interconnect?",
                "back": "- Cloud NAT: Lets private VMs access internet without external IPs (egress only)\n- Cloud VPN: Encrypted tunnel over public internet to on-prem (up to 3 Gbps per tunnel)\n- Dedicated Interconnect: Physical connection, 10/100 Gbps, 99.99% SLA\n- Partner Interconnect: Via service provider, 50 Mbps-50 Gbps\n- Use Interconnect for high bandwidth, VPN for quick setup"
            },
            {
                "category": "Deployment",
                "front": "Cloud Deployment Manager vs Terraform?",
                "back": "- Deployment Manager: GCP-native IaC, uses YAML/Jinja2/Python templates\n- Terraform: Multi-cloud IaC by HashiCorp, uses HCL language\n- Both support preview/plan before applying changes\n- Deployment Manager is free, tightly integrated with GCP\n- Terraform is the industry standard, supports 100+ providers"
            },
            {
                "category": "Storage",
                "front": "Persistent Disk types in GCP?",
                "back": "- pd-standard: HDD-backed, lowest cost, sequential I/O\n- pd-balanced: SSD-backed, cost-effective, general purpose\n- pd-ssd: SSD-backed, highest IOPS for random access\n- pd-extreme: Highest performance, configurable IOPS (up to 120K)\n- Regional PDs: Replicated across 2 zones for HA\n- Local SSD: Physically attached, ephemeral, highest throughput"
            }
        ],
        "google-professional-cloud-developer": [
            {
                "category": "Serverless",
                "front": "What is Cloud Run and how does it scale?",
                "back": "- Fully managed serverless container platform\n- Scales automatically from 0 to thousands of instances based on traffic\n- Can configure min-instances to avoid cold starts\n- Supports any language, runtime, or binary via container images\n- Pay-per-use: billed only when container processes requests (100ms granularity)"
            },
            {
                "category": "CI/CD",
                "front": "What is Cloud Build and how do you configure it?",
                "back": "- Serverless CI/CD platform that executes builds on Google infrastructure\n- Configured via a `cloudbuild.yaml` or `cloudbuild.json` file\n- Consists of sequential build steps, each running in a Docker container\n- Integrates with GitHub/Bitbucket to trigger builds on code pushes\n- Can build, test, and deploy containerized/non-containerized applications"
            },
            {
                "category": "Registry",
                "front": "Artifact Registry vs Container Registry?",
                "back": "- Artifact Registry is the evolution of Container Registry (deprecating GCR)\n- Supports Docker container images AND language packages (npm, pip, maven, NuGet)\n- Supports regional repositories and fine-grained IAM permissions\n- Integrated vulnerability scanning for container images\n- Repository URL format: REGION-docker.pkg.dev/PROJECT-ID/REPO-NAME"
            },
            {
                "category": "Secrets",
                "front": "How do you manage secrets securely in Google Cloud?",
                "back": "- Use Secret Manager to store API keys, passwords, credentials, and other credentials\n- Secrets are versioned and encrypted at rest\n- Grant permissions using IAM role `roles/secretmanager.secretAccessor` to service accounts\n- Inject secrets into Cloud Run/Functions as environment variables or mount as volumes\n- Avoid storing secrets in source code, configuration files, or container images"
            },
            {
                "category": "Observability",
                "front": "Cloud Trace vs Cloud Profiler vs Cloud Debugger?",
                "back": "- Cloud Trace: Distributed tracing system that tracks latency across microservices\n- Cloud Profiler: Continuous profiling of CPU/memory usage inside application code to optimize performance\n- Cloud Debugger: Inspect application state without stopping the app (deprecated, replaced by OpenTelemetry/third-party alternatives)\n- Use Trace to find bottlenecks, Profiler to optimize resource utilization"
            },
            {
                "category": "Observability",
                "front": "How does Error Reporting help developers?",
                "back": "- Automatically aggregates crash details and stack traces from running services\n- Group similar errors together and sends alerts on new exceptions\n- Supports major languages (Python, Go, Node.js, Java, etc.)\n- Link errors directly to source code repositories or bug trackers\n- Displays occurrence rates and affected user metrics"
            },
            {
                "category": "Messaging",
                "front": "Cloud Pub/Sub push vs pull subscriptions?",
                "back": "- Pull subscription: Consumers request messages from Pub/Sub (ideal for batch/large volume)\n- Push subscription: Pub/Sub delivers messages to a webhook HTTPS endpoint (ideal for serverless/low latency)\n- Push subscriptions require registering a verified domain or using service account tokens for authentication\n- Messages are retained up to 7 days by default if unacknowledged"
            },
            {
                "category": "Task Queues",
                "front": "Cloud Tasks: What is it and when to use?",
                "back": "- Asynchronous task execution service with rate-limiting and scheduling\n- Use to offload long-running background tasks from HTTP requests\n- Supports task de-duplication, retries, and scheduled execution times\n- Targets HTTP endpoints (e.g., Cloud Run, Cloud Functions) or App Engine queue handlers\n- Bounded queue rates prevent overwhelming downstream services"
            },
            {
                "category": "Deployment",
                "front": "Deployment strategies: Blue-Green vs Canary?",
                "back": "- Blue-Green: Maintain two identical environments. Deploy to Green, test, then switch traffic 100% (fast rollback)\n- Canary: Deploy changes to a small subset of instances (e.g., 5% of traffic), monitor errors, then gradually roll out to 100%\n- Cloud Run supports traffic splitting for easy canary testing\n- GKE supports canary deployments using Kubernetes Services and multiple Deployments"
            },
            {
                "category": "Databases",
                "front": "How do you connect to Cloud SQL securely from microservices?",
                "back": "- Use Cloud SQL Auth Proxy as a sidecar or background process\n- Proxy uses IAM credentials to authenticate and establish a secure TLS tunnel\n- Eliminates the need to allowlist client IP addresses or manage SSL certs manually\n- Connection string format: `/cloudsql/PROJECT-ID:REGION:INSTANCE-ID`\n- Use private IP within a shared VPC for direct, secure routing"
            },
            {
                "category": "IAM",
                "front": "What is IAM database authentication?",
                "back": "- Allows users or service accounts to log into Cloud SQL (PostgreSQL/MySQL) using IAM credentials\n- Eliminates hardcoded database usernames and passwords\n- Leverages OAuth2 access tokens which are short-lived and automatically rotated\n- Simplifies permission management via centralized IAM roles"
            },
            {
                "category": "App Engine",
                "front": "App Engine Standard vs App Engine Flexible?",
                "back": "- Standard: Fast startup, scales to zero, sandboxed runtimes (Python, Java, Go, etc.), limited libraries\n- Flexible: Runs custom Docker containers, uses VMs, slow startup, minimum 1 instance, no scaling to zero\n- Choose Standard for cost-sensitive, standard web applications\n- Choose Flexible for custom binaries, background threads, or writing to disk"
            },
            {
                "category": "Compute",
                "front": "What is Cloud Functions and when to use?",
                "back": "- Event-driven serverless FaaS (Function-as-a-Service)\n- Executes single-purpose code in response to events (e.g., GCS upload, Pub/Sub message, HTTP request)\n- Automatically manages scaling, patching, and OS maintenance\n- Billed per 100ms and execution count\n- Use for lightweight processing, webhooks, or file conversions"
            },
            {
                "category": "Security",
                "front": "What is Identity-Aware Proxy (IAP) for developers?",
                "back": "- Secures access to applications running on App Engine, Compute Engine, or GKE\n- Intercepts requests, validates user identity via Google Accounts, and checks IAM permissions\n- Eliminates the need for a corporate VPN to secure internal development/staging tools\n- Passes user identity headers (`x-goog-authenticated-user-email`) to the application"
            },
            {
                "category": "Security",
                "front": "VPC Service Controls: Developer impact?",
                "back": "- Mitigates data exfiltration risk by blocking service API calls crossing network perimeters\n- Can cause application API calls (e.g., Cloud Storage read, BigQuery insert) to fail with a 403 error if not inside the perimeter\n- Developers must configure access levels or ingress/egress rules to allow legitimate cross-perimeter traffic"
            }
        ],
        "google-cloud-digital-leader": [
            {
                "category": "Cloud Concepts",
                "front": "CapEx vs OpEx in cloud computing?",
                "back": "- CapEx (Capital Expenditure): Upfront investment in physical infrastructure\n- OpEx (Operational Expenditure): Pay-as-you-go cloud spending\n- Cloud shifts IT from CapEx to OpEx model\n- Benefits: No upfront cost, scale on demand, pay only for what you use\n- Reduces financial risk of overprovisioning"
            },
            {
                "category": "Cloud Concepts",
                "front": "Public vs Private vs Hybrid vs Multi-cloud?",
                "back": "- Public cloud: Resources shared across tenants (GCP, AWS, Azure)\n- Private cloud: Dedicated infrastructure for one organization\n- Hybrid cloud: Mix of on-premises and public cloud\n- Multi-cloud: Using multiple public cloud providers\n- Anthos enables hybrid/multi-cloud Kubernetes management"
            },
            {
                "category": "Cloud Concepts",
                "front": "What is Total Cost of Ownership (TCO)?",
                "back": "- Full cost of owning and operating IT infrastructure\n- Includes: Hardware, software, personnel, power, cooling, facility\n- Cloud TCO eliminates facility/hardware costs\n- Google TCO calculator helps compare on-prem vs cloud\n- Hidden on-prem costs: Maintenance, upgrades, downtime"
            },
            {
                "category": "Data & AI",
                "front": "BigQuery: What is it and key features?",
                "back": "- Serverless, petabyte-scale data warehouse\n- Uses SQL for querying structured and semi-structured data\n- Columnar storage with automatic optimization\n- Supports ML models directly via BigQuery ML\n- Pricing: On-demand ($5/TB scanned) or flat-rate (slots)\n- Separation of storage and compute"
            },
            {
                "category": "Data & AI",
                "front": "Structured vs Unstructured vs Semi-structured data?",
                "back": "- Structured: Organized in rows/columns (SQL databases, spreadsheets)\n- Unstructured: No predefined format (images, videos, PDFs, audio)\n- Semi-structured: Has tags/markers but no rigid schema (JSON, XML, Avro)\n- Cloud Storage: Best for unstructured data\n- BigQuery/Cloud SQL: Best for structured data"
            },
            {
                "category": "Data & AI",
                "front": "Data lake vs Data warehouse?",
                "back": "- Data lake: Raw data in any format, schema-on-read (Cloud Storage)\n- Data warehouse: Processed, structured data, schema-on-write (BigQuery)\n- Data lakes store everything, warehouses store curated analytics data\n- Lakehouse: Combines both approaches (BigLake)\n- Data lakes are cheaper for storage, warehouses are faster for queries"
            },
            {
                "category": "Infrastructure",
                "front": "GCP compute options comparison?",
                "back": "- Compute Engine: Full VMs (IaaS) - most control\n- GKE: Managed Kubernetes - container orchestration\n- App Engine: PaaS - just deploy code\n- Cloud Run: Serverless containers - scales to zero\n- Cloud Functions: FaaS - event-driven, single-purpose\n- More managed = less control but less operational burden"
            },
            {
                "category": "Infrastructure",
                "front": "GCP global infrastructure hierarchy?",
                "back": "- Regions: Independent geographic areas (e.g., us-central1)\n- Zones: Isolated locations within regions (e.g., us-central1-a)\n- 40+ regions, 121+ zones worldwide\n- Multi-region: Services spanning multiple regions (e.g., Cloud Storage)\n- Edge locations: Google's CDN points of presence (PoPs)"
            },
            {
                "category": "Security",
                "front": "Shared Responsibility Model?",
                "back": "- Google secures: Physical infrastructure, hardware, network, encryption at rest\n- Customer secures: Data, access policies, application security, IAM configuration\n- Shared: OS patches (depends on service), network config\n- More managed services = more Google responsibility\n- IaaS: Customer manages most; SaaS: Google manages most"
            },
            {
                "category": "Security",
                "front": "Google Cloud encryption at rest and in transit?",
                "back": "- All data encrypted at rest by default (AES-256)\n- All data encrypted in transit between Google data centers\n- HTTPS enforced for all GCP APIs\n- Customer-managed encryption keys (CMEK): You control keys in Cloud KMS\n- Customer-supplied encryption keys (CSEK): You provide your own keys"
            },
            {
                "category": "Migration",
                "front": "Cloud migration strategies (the 6 Rs)?",
                "back": "- Rehost (Lift & Shift): Move as-is to cloud VMs\n- Replatform: Minor optimizations (e.g., managed DB)\n- Refactor: Rewrite for cloud-native architecture\n- Repurchase: Switch to SaaS solution\n- Retire: Decommission unused systems\n- Retain: Keep on-premises (not ready to migrate)"
            },
            {
                "category": "AI/ML",
                "front": "Pre-trained AI APIs in Google Cloud?",
                "back": "- Vision AI: Image classification, OCR, face detection\n- Natural Language AI: Sentiment analysis, entity recognition\n- Speech-to-Text / Text-to-Speech: Audio transcription\n- Translation AI: 100+ languages\n- Video AI: Object tracking, shot detection\n- No ML expertise needed to use these APIs"
            },
            {
                "category": "Operations",
                "front": "SLA vs SLO vs SLI?",
                "back": "- SLA (Service Level Agreement): Contract with penalties if not met\n- SLO (Service Level Objective): Internal reliability target\n- SLI (Service Level Indicator): Actual measured metric (e.g., latency)\n- Example: SLI = 99.95% uptime, SLO = 99.9%, SLA = 99.5%\n- SLOs should be stricter than SLAs to catch issues early"
            },
            {
                "category": "Sustainability",
                "front": "Google Cloud sustainability commitments?",
                "back": "- Carbon neutral since 2007\n- Goal: Run on 24/7 carbon-free energy by 2030\n- Carbon Footprint tool shows emissions per project\n- Region Picker considers carbon impact\n- Cloud is 1.5-3x more energy efficient than on-prem data centers"
            },
            {
                "category": "Cost Management",
                "front": "GCP cost optimization strategies?",
                "back": "- Right-sizing recommendations from Recommender\n- Committed Use Discounts (CUDs): 1-3 year commit for savings\n- Preemptible/Spot VMs for fault-tolerant workloads\n- Cloud Storage lifecycle rules to auto-transition classes\n- Budget alerts and billing export to BigQuery\n- Autoscaling to match demand"
            }
        ],
        "google-generative-ai-leader": [
            {
                "category": "Gen AI Fundamentals",
                "front": "Generative AI vs Discriminative AI?",
                "back": "- Generative AI: Creates new content (text, images, code, audio)\n- Discriminative AI: Classifies/predicts from existing data\n- Gen AI models learn patterns from training data to generate novel outputs\n- Examples: GPT, Gemini (generative) vs spam filters, classifiers (discriminative)\n- Foundation models are large generative models trained on broad datasets"
            },
            {
                "category": "Gen AI Fundamentals",
                "front": "What are tokens and context windows?",
                "back": "- Tokens: Basic units of text (words, subwords, characters) processed by LLMs\n- 1 token ≈ 4 characters or ¾ of a word in English\n- Context window: Max tokens the model can process in one request\n- Gemini 1.5 Pro: Up to 2 million tokens context window\n- Larger context = more information but higher cost and latency"
            },
            {
                "category": "Gen AI Fundamentals",
                "front": "What is temperature in LLM inference?",
                "back": "- Controls randomness/creativity of model outputs\n- Temperature 0: Deterministic, most probable response\n- Temperature 1: More creative, diverse responses\n- Temperature > 1: Very random, potentially incoherent\n- Low temp for factual tasks, high temp for creative writing"
            },
            {
                "category": "Gen AI Fundamentals",
                "front": "What are hallucinations in Gen AI?",
                "back": "- Model generates plausible but factually incorrect information\n- Causes: Training data gaps, pattern extrapolation, lack of grounding\n- Mitigation: RAG (grounding with external data), temperature tuning\n- Fact-checking, human-in-the-loop review\n- Grounding with Google Search or enterprise data reduces hallucinations"
            },
            {
                "category": "Vertex AI",
                "front": "What is Vertex AI and its key components?",
                "back": "- Google Cloud's unified ML/AI development platform\n- Vertex AI Studio: Prompt design, tuning, and testing UI\n- Model Garden: Access to 100+ foundation and open-source models\n- Vertex AI Agent Builder: Build AI agents with search and conversation\n- Vertex AI Pipelines: MLOps orchestration for production ML"
            },
            {
                "category": "Vertex AI",
                "front": "Vertex AI Model Garden vs Vertex AI Studio?",
                "back": "- Model Garden: Catalog of pre-trained models (Gemini, PaLM, Llama, Mistral)\n- Deploy, fine-tune, or evaluate models from the garden\n- Vertex AI Studio: Interactive UI for prompt engineering\n- Test prompts, adjust parameters, compare model outputs\n- Studio is for prototyping; Garden is for model selection"
            },
            {
                "category": "Prompting",
                "front": "Prompt engineering techniques?",
                "back": "- Zero-shot: Direct instruction with no examples\n- Few-shot: Provide examples of desired input/output pairs\n- Chain-of-Thought (CoT): Ask model to show reasoning steps\n- System prompts: Set model persona, constraints, and format\n- Best practice: Be specific, provide context, iterate on prompts"
            },
            {
                "category": "RAG",
                "front": "What is RAG (Retrieval-Augmented Generation)?",
                "back": "- Combines LLM generation with external knowledge retrieval\n- Steps: Query → Retrieve relevant docs → Augment prompt → Generate answer\n- Reduces hallucinations by grounding responses in real data\n- Uses vector databases and embeddings for semantic search\n- Better than fine-tuning for rapidly changing information"
            },
            {
                "category": "RAG",
                "front": "What are embeddings and vector databases?",
                "back": "- Embeddings: Dense numerical representations of text/images/data\n- Capture semantic meaning (similar concepts are close in vector space)\n- Vector databases: Specialized stores for similarity search (Vertex AI Vector Search)\n- Used in RAG to find relevant documents for a query\n- Dimensionality typically 256-1536 for text embeddings"
            },
            {
                "category": "Business",
                "front": "Common Gen AI enterprise use cases?",
                "back": "- Customer service: AI chatbots, email response drafting\n- Content creation: Marketing copy, product descriptions\n- Code generation: Code completion, bug fixing, documentation\n- Search: Enterprise knowledge base with natural language queries\n- Summarization: Meeting notes, document summaries, report generation"
            },
            {
                "category": "Business",
                "front": "Build vs Buy decisions for Gen AI?",
                "back": "- Buy (API): Use Gemini API for standard tasks, fastest time-to-value\n- Customize: Fine-tune a foundation model on your data\n- Build: Train from scratch (requires massive data and compute)\n- Most enterprises should start with API + RAG\n- Build only when unique domain data gives competitive advantage"
            },
            {
                "category": "Responsible AI",
                "front": "Google's Responsible AI Principles?",
                "back": "- Be socially beneficial\n- Avoid creating or reinforcing unfair bias\n- Be built and tested for safety\n- Be accountable to people\n- Incorporate privacy design principles\n- Uphold high standards of scientific excellence\n- Google will NOT develop AI for: weapons, surveillance violating norms, harm"
            },
            {
                "category": "Responsible AI",
                "front": "AI safety filters and governance?",
                "back": "- Safety filters block harmful content (violence, hate speech, PII)\n- Configurable thresholds: Block None, Block Few, Block Some, Block Most\n- Content moderation classifiers score output toxicity\n- Data governance: Control what training data is used\n- Audit logging tracks all model invocations and outputs"
            },
            {
                "category": "Gemini",
                "front": "Gemini model family and capabilities?",
                "back": "- Gemini Ultra/Pro/Flash: Different performance vs cost tradeoffs\n- Natively multimodal: Text, images, audio, video, code\n- Gemini Flash: Fastest, lowest cost, best for high-volume tasks\n- Gemini Pro: Balanced performance for complex reasoning\n- Available via Vertex AI API and Google AI Studio"
            },
            {
                "category": "Fine-tuning",
                "front": "Fine-tuning vs Prompt engineering vs RAG?",
                "back": "- Prompt engineering: Cheapest, fastest, no training needed\n- RAG: Adds external knowledge at inference time, no retraining\n- Fine-tuning: Adapts model weights with custom data, expensive\n- Prompt engineering first → RAG if knowledge needed → Fine-tune if style/format critical\n- Fine-tuning changes the model; RAG changes the context"
            }
        ],
        "google-professional-cloud-architect": [
            {
                "category": "Design",
                "front": "Designing for high availability on GCP?",
                "back": "- Use regional Managed Instance Groups across zones\n- Regional GKE clusters for container workloads\n- Cloud Spanner or multi-region Cloud Storage for data\n- Global HTTP(S) Load Balancer for traffic distribution\n- Design for failure: assume any component can fail"
            },
            {
                "category": "Design",
                "front": "Microservices vs Monolithic architecture?",
                "back": "- Monolithic: Single deployable unit, simpler but harder to scale\n- Microservices: Independent services communicating via APIs\n- GCP tools: Cloud Run, GKE for microservices deployment\n- Pub/Sub for async communication between services\n- Each service can scale independently and use different languages"
            },
            {
                "category": "Networking",
                "front": "Shared VPC vs VPC Peering?",
                "back": "- Shared VPC: Central network admin, projects share a host VPC\n- VPC Peering: Connect two separate VPCs, non-transitive\n- Shared VPC: Best for organizations with centralized networking\n- VPC Peering: Best for connecting independent projects\n- Shared VPC supports IAM control; Peering is simpler setup"
            },
            {
                "category": "Security",
                "front": "Defense in depth strategy on GCP?",
                "back": "- Network: VPC firewall rules, Cloud Armor DDoS protection\n- Identity: IAM, Identity-Aware Proxy (IAP), MFA\n- Data: Encryption at rest (default), CMEK, DLP API\n- Application: Web Security Scanner, Binary Authorization\n- Operations: Cloud Audit Logs, Security Command Center\n- Multiple overlapping layers of security controls"
            },
            {
                "category": "Migration",
                "front": "GCP migration tools?",
                "back": "- Migrate for Compute Engine: VM migrations from on-prem/other clouds\n- Migrate for Anthos: Modernize VMs to containers\n- Database Migration Service: MySQL, PostgreSQL, SQL Server\n- Transfer Service: Large-scale data transfer to Cloud Storage\n- BigQuery Data Transfer Service: SaaS data into BigQuery"
            },
            {
                "category": "Data",
                "front": "When to use Cloud Bigtable vs BigQuery?",
                "back": "- Bigtable: Low-latency NoSQL for high-throughput read/write (IoT, time-series)\n- BigQuery: Analytics warehouse for complex SQL queries on large datasets\n- Bigtable: Single-digit ms latency, row-key based access\n- BigQuery: Seconds-minutes latency, columnar storage\n- Bigtable for operational data; BigQuery for analytical data"
            },
            {
                "category": "Reliability",
                "front": "Disaster recovery patterns on GCP?",
                "back": "- Cold: Backup data only, longest RTO (hours-days)\n- Warm: Scaled-down environment ready to scale up, moderate RTO\n- Hot: Fully running duplicate environment, shortest RTO (minutes)\n- Dual-region: Active-active across regions for near-zero RTO\n- RPO determined by backup/replication frequency"
            },
            {
                "category": "Cost",
                "front": "Cost optimization best practices?",
                "back": "- Right-size VMs using Recommender\n- Use CUDs for predictable workloads (up to 57% off)\n- Spot VMs for fault-tolerant batch processing\n- Autoscaling to match demand\n- Storage lifecycle policies to transition to cheaper tiers\n- Export billing to BigQuery for analysis"
            },
            {
                "category": "Compliance",
                "front": "GCP compliance and data residency?",
                "back": "- Resource Location Restriction org policy: Enforce data residency\n- VPC Service Controls: Prevent data exfiltration\n- Access Transparency: Logs of Google admin access to your data\n- Assured Workloads: Pre-configured compliance environments\n- Supports HIPAA, PCI-DSS, SOC 2, ISO 27001, FedRAMP"
            },
            {
                "category": "Architecture",
                "front": "Event-driven architecture on GCP?",
                "back": "- Pub/Sub: Async messaging between services (at-least-once delivery)\n- Eventarc: Route events from GCP services to targets\n- Cloud Functions: Respond to events (HTTP, Pub/Sub, Cloud Storage)\n- Cloud Tasks: Managed task queues with rate limiting\n- Workflows: Orchestrate multi-service processes"
            },
            {
                "category": "Architecture",
                "front": "API management with Apigee?",
                "back": "- Full lifecycle API management platform\n- API gateway, analytics, monetization, developer portal\n- Rate limiting, quotas, OAuth/API key security\n- API versioning and traffic management\n- Use for external-facing APIs with partner/developer access"
            },
            {
                "category": "Hybrid",
                "front": "Anthos for hybrid and multi-cloud?",
                "back": "- Manage GKE clusters on-prem, AWS, Azure from single control plane\n- Anthos Config Management: GitOps-based policy enforcement\n- Anthos Service Mesh: Observability and security for microservices\n- Migrate for Anthos: Convert VMs to containers\n- Consistent Kubernetes experience across environments"
            },
            {
                "category": "Identity",
                "front": "Cloud Identity and Workspace federation?",
                "back": "- Cloud Identity: IDaaS for managing users and groups\n- Workforce Identity Federation: External IdP users access GCP\n- Workload Identity Federation: External workloads access GCP (no service account keys)\n- Google Cloud Directory Sync: Sync from Active Directory/LDAP\n- SSO with SAML 2.0 or OIDC"
            },
            {
                "category": "Networking",
                "front": "GCP load balancing options?",
                "back": "- Global HTTP(S) LB: Layer 7, URL-based routing, SSL termination\n- Regional TCP/UDP LB (Network LB): Layer 4, pass-through\n- Internal TCP/UDP LB: Private load balancing within VPC\n- SSL Proxy LB: Global Layer 4 for SSL traffic\n- TCP Proxy LB: Global Layer 4 for non-SSL TCP traffic"
            },
            {
                "category": "Data",
                "front": "Cloud Memorystore: Redis and Memcached?",
                "back": "- Fully managed in-memory data store\n- Redis: Rich data structures, persistence, pub/sub, replication\n- Memcached: Simple key-value caching, multi-threaded\n- Use cases: Session caching, leaderboards, rate limiting\n- Sub-millisecond latency for read-heavy workloads"
            }
        ],
        "google-professional-data-engineer": [
            {
                "category": "Data Processing",
                "front": "Dataflow vs Dataproc?",
                "back": "- Dataflow: Fully managed, Apache Beam-based, serverless\n- Dataproc: Managed Hadoop/Spark clusters, configurable\n- Dataflow: Best for new pipelines, auto-scaling, streaming\n- Dataproc: Best for existing Hadoop/Spark workloads migration\n- Dataflow handles windowing and watermarks natively"
            },
            {
                "category": "Data Processing",
                "front": "Pub/Sub: Key concepts and guarantees?",
                "back": "- Global, real-time messaging service\n- At-least-once delivery (pull or push subscriptions)\n- Message retention: Up to 31 days\n- Ordering with ordering keys\n- Dead letter topics for failed messages\n- Exactly-once processing with Dataflow integration"
            },
            {
                "category": "Data Processing",
                "front": "Apache Beam windowing types?",
                "back": "- Fixed windows: Non-overlapping, fixed duration (e.g., every 5 min)\n- Sliding windows: Overlapping, defined by duration + period\n- Session windows: Based on activity gaps per key\n- Global window: Single window for all data (default)\n- Watermarks track event-time progress for late data handling"
            },
            {
                "category": "Storage",
                "front": "BigQuery partitioning and clustering?",
                "back": "- Partitioning: Divides table by date/integer range, reduces scan cost\n- Clustering: Sorts data within partitions by up to 4 columns\n- Partition pruning: Only scans relevant partitions\n- Clustering improves filter and aggregate query performance\n- Best practice: Partition by date, cluster by frequently filtered columns"
            },
            {
                "category": "Storage",
                "front": "BigQuery pricing models?",
                "back": "- On-demand: $5/TB of data scanned (first 1 TB/month free)\n- Capacity (editions): Pay for dedicated compute slots\n- Storage: $0.02/GB/month (active), $0.01/GB (long-term after 90 days)\n- Streaming inserts: $0.01/200 MB\n- Use partitioning and clustering to reduce scan costs"
            },
            {
                "category": "ML",
                "front": "BigQuery ML supported model types?",
                "back": "- Linear/logistic regression\n- K-means clustering\n- Matrix factorization (recommendations)\n- Time series (ARIMA_PLUS)\n- Deep Neural Networks (TensorFlow)\n- XGBoost and random forest\n- Train directly with SQL, no data export needed"
            },
            {
                "category": "Data Quality",
                "front": "Data governance and lineage on GCP?",
                "back": "- Dataplex: Unified data governance and management\n- Data Catalog: Metadata management and discovery\n- Data Lineage: Track data flow across systems\n- DLP API: Discover and protect sensitive data (PII)\n- Column-level security in BigQuery for fine-grained access"
            },
            {
                "category": "Streaming",
                "front": "Streaming architecture on GCP?",
                "back": "- Ingest: Pub/Sub (async) or Dataflow (direct)\n- Process: Dataflow (Apache Beam) for transforms and windowing\n- Store: BigQuery (streaming buffer) or Bigtable (low-latency)\n- Analyze: BigQuery SQL or Looker dashboards\n- Pub/Sub → Dataflow → BigQuery is the canonical streaming pipeline"
            },
            {
                "category": "ETL",
                "front": "Cloud Data Fusion vs Dataflow?",
                "back": "- Data Fusion: Visual ETL pipeline builder (CDAP-based), no-code\n- Dataflow: Code-based (Apache Beam), fully serverless\n- Data Fusion: Best for business users and visual pipeline design\n- Dataflow: Best for complex custom transformations\n- Data Fusion generates Dataproc jobs under the hood"
            },
            {
                "category": "Storage",
                "front": "Bigtable schema design best practices?",
                "back": "- Design row keys to avoid hotspotting\n- Don't start row keys with timestamps (causes sequential writes)\n- Use reversed timestamps or salted keys for even distribution\n- Store related data in the same column family\n- Tall and narrow tables preferred over short and wide\n- Use row key prefixes for efficient range scans"
            },
            {
                "category": "Migration",
                "front": "Data migration strategies to BigQuery?",
                "back": "- BigQuery Data Transfer Service: Scheduled transfers from SaaS\n- Storage Transfer Service: Move from S3, Azure, or on-prem\n- gsutil/gcloud: CLI-based transfer to Cloud Storage then load\n- Dataflow: Transform during migration\n- Federation: Query external data without moving it"
            },
            {
                "category": "Security",
                "front": "BigQuery security features?",
                "back": "- Dataset-level, table-level, column-level access control\n- Row-level security with row access policies\n- Data masking with policy tags\n- Authorized views: Share query results without exposing source tables\n- CMEK for customer-managed encryption keys\n- VPC Service Controls to prevent data exfiltration"
            },
            {
                "category": "Orchestration",
                "front": "Cloud Composer: What and when?",
                "back": "- Managed Apache Airflow for workflow orchestration\n- DAGs (Directed Acyclic Graphs) define task dependencies\n- Schedule and monitor complex multi-service data pipelines\n- Integrates with BigQuery, Dataflow, Dataproc, GCS\n- Use when pipelines have complex dependencies and scheduling needs"
            },
            {
                "category": "Analytics",
                "front": "Looker vs Looker Studio (Data Studio)?",
                "back": "- Looker: Enterprise BI platform with LookML semantic layer\n- Looker Studio: Free self-service dashboarding tool\n- Looker: Governed metrics, data modeling, embedded analytics\n- Looker Studio: Quick visualizations, connects to 800+ sources\n- Use Looker for enterprise; Looker Studio for ad-hoc reporting"
            },
            {
                "category": "Data Processing",
                "front": "Dataflow templates and flex templates?",
                "back": "- Classic templates: Pre-built, Google-provided pipelines\n- Flex templates: Custom pipelines packaged as Docker containers\n- Templates allow non-developers to run pipelines\n- Flex templates support dynamic parameters and custom environments\n- Classic templates: Limited customization but faster to deploy"
            }
        ],
        "google-professional-cloud-devops-engineer": [
            {
                "category": "CI/CD",
                "front": "Cloud Build: Key features?",
                "back": "- Serverless CI/CD platform\n- Build, test, and deploy via YAML/JSON config (cloudbuild.yaml)\n- Supports Docker, Maven, Gradle, npm, Go, and more\n- Triggers: GitHub, Cloud Source Repos, Pub/Sub, webhooks\n- 120 free build-minutes/day, parallel builds supported"
            },
            {
                "category": "CI/CD",
                "front": "Cloud Deploy: What is it?",
                "back": "- Managed continuous delivery service for GKE and Cloud Run\n- Delivery pipelines with promotion through environments\n- Supports canary, blue-green, and rolling deployments\n- Approval gates between stages (dev → staging → prod)\n- Integrates with Cloud Build for CI"
            },
            {
                "category": "SRE",
                "front": "Error Budgets in SRE?",
                "back": "- Error budget = 1 - SLO (e.g., 99.9% SLO = 0.1% error budget)\n- Represents allowed unreliability per period\n- If budget is spent: freeze features, focus on reliability\n- If budget remains: ship new features faster\n- Aligns development velocity with reliability goals"
            },
            {
                "category": "SRE",
                "front": "DORA metrics for DevOps performance?",
                "back": "- Deployment Frequency: How often code is deployed\n- Lead Time for Changes: Code commit to production\n- Change Failure Rate: Percentage of deployments causing failures\n- Time to Restore Service: Recovery time from incidents\n- Elite teams: Multiple deploys/day, < 1 hour lead time"
            },
            {
                "category": "Monitoring",
                "front": "Four Golden Signals of monitoring?",
                "back": "- Latency: Time to serve a request\n- Traffic: Amount of demand on the system\n- Errors: Rate of failed requests\n- Saturation: How full the system is (CPU, memory, disk)\n- Focus dashboards and alerts on these four signals"
            },
            {
                "category": "Monitoring",
                "front": "Cloud Trace vs Cloud Profiler?",
                "back": "- Cloud Trace: Distributed tracing for request latency analysis\n- Shows end-to-end request flow across microservices\n- Cloud Profiler: Continuous CPU/memory profiling in production\n- Identifies performance bottlenecks in code\n- Trace for latency issues; Profiler for code-level optimization"
            },
            {
                "category": "Deployment",
                "front": "Blue-Green vs Canary vs Rolling deployments?",
                "back": "- Blue-Green: Two identical environments, switch traffic instantly\n- Canary: Route small % of traffic to new version, gradually increase\n- Rolling: Replace instances incrementally, no extra resources\n- Blue-Green: Fastest rollback, most resources needed\n- Canary: Safest for risk detection, slower rollout"
            },
            {
                "category": "Incident",
                "front": "Incident management best practices?",
                "back": "- Define incident severity levels (P1-P4)\n- Incident Commander coordinates response\n- Use runbooks for common failure scenarios\n- Blameless post-mortems after every significant incident\n- Document: Timeline, root cause, impact, action items\n- Cloud Error Reporting auto-groups application errors"
            },
            {
                "category": "IaC",
                "front": "Infrastructure as Code tools on GCP?",
                "back": "- Terraform: Multi-cloud, HCL language, state management\n- Cloud Deployment Manager: GCP-native, YAML templates\n- Pulumi: Programming language-based IaC\n- Config Connector: Manage GCP resources via Kubernetes\n- Best practice: Version control all infrastructure configs"
            },
            {
                "category": "Security",
                "front": "Binary Authorization for GKE?",
                "back": "- Ensures only trusted containers are deployed to GKE\n- Requires attestations (digital signatures) on container images\n- Policy enforcement at deploy time\n- Integrates with Artifact Registry vulnerability scanning\n- Break-glass mode for emergency deployments"
            },
            {
                "category": "Operations",
                "front": "Cloud Operations suite components?",
                "back": "- Cloud Monitoring: Metrics, dashboards, alerting\n- Cloud Logging: Centralized log management\n- Cloud Trace: Distributed request tracing\n- Cloud Profiler: Code-level performance profiling\n- Error Reporting: Automatic error grouping and notification\n- Cloud Debugger (deprecated): Replaced by snapshot debugging"
            },
            {
                "category": "Reliability",
                "front": "Chaos engineering on GCP?",
                "back": "- Deliberately inject failures to test system resilience\n- Test: Network partitions, VM crashes, zone outages\n- Verify auto-healing, failover, and alerting work correctly\n- Start with game days (planned chaos experiments)\n- Tools: Chaos Monkey, Litmus, Gremlin\n- Run in pre-production first, then production with safeguards"
            },
            {
                "category": "Logging",
                "front": "Log-based metrics and alerts?",
                "back": "- Create custom metrics from log entries via filters\n- Counter metrics: Count log entries matching a filter\n- Distribution metrics: Track numeric values from logs\n- Use log-based metrics to trigger Cloud Monitoring alerts\n- Example: Alert on error count exceeding threshold"
            },
            {
                "category": "Testing",
                "front": "Testing strategies for reliability?",
                "back": "- Unit tests: Individual function/method validation\n- Integration tests: Service interaction verification\n- Load tests: Capacity and performance under stress\n- Canary analysis: Compare canary metrics to baseline\n- Disaster recovery drills: Validate failover procedures\n- Shift-left: Test early in development pipeline"
            },
            {
                "category": "Containers",
                "front": "Artifact Registry vs Container Registry?",
                "back": "- Artifact Registry: Current, recommended service\n- Supports Docker, Maven, npm, Python, Go, Apt, Yum\n- Regional and multi-regional repositories\n- Vulnerability scanning with Artifact Analysis\n- Container Registry: Legacy, Docker-only, being deprecated\n- Always use Artifact Registry for new projects"
            }
        ],
        "google-professional-cloud-security-engineer": [
            {
                "category": "IAM",
                "front": "IAM Conditions and Context-Aware Access?",
                "back": "- IAM Conditions: Grant access based on attributes (time, resource, IP)\n- Context-Aware Access: Access decisions based on user identity AND device security\n- BeyondCorp Enterprise: Zero-trust security model\n- Access Levels: Define trust criteria (device encryption, OS version)\n- Enforced via Identity-Aware Proxy (IAP)"
            },
            {
                "category": "Network Security",
                "front": "VPC Service Controls?",
                "back": "- Create security perimeters around GCP resources\n- Prevents data exfiltration from authorized APIs\n- Service perimeter: Defines which projects and services are protected\n- Access levels and ingress/egress rules for exceptions\n- Dry-run mode to test before enforcement"
            },
            {
                "category": "Network Security",
                "front": "Cloud Armor: DDoS and WAF?",
                "back": "- DDoS protection for HTTP(S) Load Balancer\n- WAF rules: OWASP Top 10 protection, SQL injection, XSS\n- Adaptive Protection: ML-based attack detection\n- Rate limiting and bot management\n- Geo-based access control (allow/deny by country)\n- Pre-configured rules for common attack patterns"
            },
            {
                "category": "Data Security",
                "front": "Cloud DLP API capabilities?",
                "back": "- Discover, classify, and de-identify sensitive data\n- 150+ built-in info types (SSN, credit cards, email, etc.)\n- De-identification: Masking, tokenization, bucketing\n- Scan: Cloud Storage, BigQuery, Datastore\n- Risk analysis for quasi-identifiers (k-anonymity, l-diversity)"
            },
            {
                "category": "Data Security",
                "front": "Cloud KMS encryption options?",
                "back": "- Google-managed keys: Default, no configuration needed\n- Customer-managed keys (CMEK): You control key rotation/destruction\n- Customer-supplied keys (CSEK): You provide keys, Google doesn't store them\n- Cloud HSM: Hardware security modules for FIPS 140-2 Level 3\n- Cloud EKM: Keys managed in external key management system"
            },
            {
                "category": "Identity",
                "front": "Workload Identity Federation?",
                "back": "- Allow external workloads (AWS, Azure, GitHub Actions) to access GCP\n- No service account key management needed\n- Uses OIDC or SAML tokens from external IdP\n- Maps external identities to GCP IAM principals\n- Recommended over downloading service account keys"
            },
            {
                "category": "Compliance",
                "front": "Security Command Center (SCC)?",
                "back": "- Centralized security and risk management dashboard\n- Standard tier: Vulnerability scanning, compliance monitoring\n- Premium tier: Threat detection, container security, Event Threat Detection\n- Security Health Analytics: Misconfiguration detection\n- Web Security Scanner: OWASP vulnerability scanning\n- Findings: Unified view of security issues across all projects"
            },
            {
                "category": "Audit",
                "front": "Cloud Audit Logs types?",
                "back": "- Admin Activity: Who did what admin action (always on, free, 400-day retention)\n- Data Access: Who accessed data (must enable, charged, 30-day default)\n- System Event: Google-initiated actions (always on, free, 400-day)\n- Policy Denied: Actions denied by policies (always on, free)\n- Export logs via sinks to Cloud Storage, BigQuery, or Pub/Sub"
            },
            {
                "category": "Network Security",
                "front": "Private Google Access and Private Service Connect?",
                "back": "- Private Google Access: VMs without external IPs access Google APIs\n- Enabled per subnet, routes traffic via internal network\n- Private Service Connect: Private endpoint for Google APIs in your VPC\n- Creates a consumer endpoint with an internal IP\n- Keeps all traffic on Google's private network"
            },
            {
                "category": "Zero Trust",
                "front": "BeyondCorp Enterprise components?",
                "back": "- Zero-trust security model: Never trust, always verify\n- Identity-Aware Proxy (IAP): Per-request authentication and authorization\n- Access Context Manager: Define device and network conditions\n- Endpoint Verification: Inventory and assess device compliance\n- No VPN needed for secure application access"
            },
            {
                "category": "Container Security",
                "front": "GKE security best practices?",
                "back": "- Enable Workload Identity for pod-level IAM\n- Use Binary Authorization for trusted images only\n- Enable Shielded GKE Nodes (Secure Boot, vTPM)\n- Network Policies to restrict pod-to-pod traffic\n- Private clusters: No public IPs on nodes\n- Regular vulnerability scanning with Artifact Analysis"
            },
            {
                "category": "Secrets",
                "front": "Secret Manager vs Cloud KMS?",
                "back": "- Secret Manager: Store and access secrets (passwords, API keys, certs)\n- Cloud KMS: Manage encryption keys (encrypt/decrypt operations)\n- Secret Manager stores the secret value itself\n- KMS stores keys that encrypt data (you manage the encrypted data)\n- Use both together: Secret Manager encrypted with CMEK"
            },
            {
                "category": "Supply Chain",
                "front": "Software supply chain security on GCP?",
                "back": "- Artifact Registry: Store and scan container images\n- Binary Authorization: Only deploy attested images\n- Cloud Build: Provenance attestation (SLSA compliance)\n- Container Analysis: Vulnerability scanning of images\n- SLSA framework: Levels 1-4 of supply chain security maturity"
            },
            {
                "category": "Organization",
                "front": "Organization Policy Service?",
                "back": "- Centralized constraints across GCP organization\n- Resource location restriction: Enforce data residency\n- Disable service account key creation\n- Enforce uniform bucket-level access\n- Restrict VM external IP addresses\n- Inherited down the org hierarchy, overridable at lower levels"
            },
            {
                "category": "Threat Detection",
                "front": "Event Threat Detection and Chronicle?",
                "back": "- Event Threat Detection: Scans logs for threats (crypto mining, malware, IAM anomalies)\n- Chronicle: Google's security analytics platform (SIEM/SOAR)\n- Chronicle ingests massive log volumes for threat hunting\n- Integrates with SCC for unified security management\n- Uses Google threat intelligence for detection rules"
            }
        ],
        "google-professional-cloud-network-engineer": [
            {
                "category": "VPC",
                "front": "VPC auto-mode vs custom-mode?",
                "back": "- Auto-mode: Automatically creates subnets in each region (10.128.0.0/9)\n- Custom-mode: No auto subnets, you define all CIDR ranges\n- Auto-mode: Good for quick setup, limited CIDR control\n- Custom-mode: Production recommended, full control\n- Can convert auto to custom (one-way, irreversible)"
            },
            {
                "category": "VPC",
                "front": "VPC flow logs?",
                "back": "- Capture IP traffic metadata for VPC subnets\n- Logged per VM network interface every 5 seconds (configurable)\n- Use cases: Network monitoring, forensics, compliance\n- Aggregation interval: 5s, 30s, 1min, 5min, 10min, 15min\n- Sample rate: 50% default, configurable 0-100%\n- Stored in Cloud Logging, exportable to BigQuery"
            },
            {
                "category": "Load Balancing",
                "front": "Internal vs External Load Balancing?",
                "back": "- External: Distributes internet traffic to backends\n- Internal: Distributes internal/private traffic within VPC\n- External HTTP(S): Global, Layer 7, URL routing\n- Internal TCP/UDP: Regional, Layer 4, passthrough\n- Internal HTTP(S): Regional, Layer 7, proxy-based\n- Cross-region internal LB available with Premium Tier"
            },
            {
                "category": "DNS",
                "front": "Cloud DNS: Key features?",
                "back": "- Managed authoritative DNS service (100% SLA)\n- Public zones: Internet-facing domain resolution\n- Private zones: Internal DNS within VPC networks\n- DNS forwarding: Route queries to on-prem DNS servers\n- DNS peering: Share private zones across VPC networks\n- DNSSEC: Cryptographic validation of DNS responses"
            },
            {
                "category": "Connectivity",
                "front": "Cloud Interconnect options?",
                "back": "- Dedicated Interconnect: Physical connection 10/100 Gbps, 99.99% SLA\n- Partner Interconnect: Via service provider 50 Mbps-50 Gbps\n- Cross-Cloud Interconnect: Direct connection to other clouds\n- Requires LOA-CFA and colocation facility for Dedicated\n- VLAN attachments connect Interconnect to VPC\n- Supports BGP for dynamic routing"
            },
            {
                "category": "Connectivity",
                "front": "Cloud VPN: HA VPN vs Classic VPN?",
                "back": "- HA VPN: 99.99% SLA, 2 interfaces per gateway, dynamic routing (BGP)\n- Classic VPN: 99.9% SLA, single interface, static or dynamic routing\n- HA VPN: Recommended for production, redundant tunnels\n- Each tunnel supports up to 3 Gbps\n- IKEv2 encryption with pre-shared keys or certificates"
            },
            {
                "category": "Routing",
                "front": "Cloud Router and BGP?",
                "back": "- Fully managed BGP router for dynamic route exchange\n- Learns routes from on-prem and propagates to VPC\n- Supports graceful restart for BGP session resilience\n- ASN: Private range 64512-65534 for GCP\n- Custom route advertisements for selective prefix sharing\n- Required for HA VPN and Interconnect"
            },
            {
                "category": "Security",
                "front": "Hierarchical firewall policies?",
                "back": "- Applied at organization or folder level\n- Override or supplement VPC-level firewall rules\n- Actions: Allow, Deny, Go to next (delegate to lower level)\n- Priority-based evaluation (lower number = higher priority)\n- Enables centralized network security governance\n- Target: All VMs or specific service accounts"
            },
            {
                "category": "Networking",
                "front": "Network Service Tiers?",
                "back": "- Premium Tier (default): Google's global backbone, optimal routing\n- Standard Tier: Regular internet routing, regional LBs only\n- Premium: Lower latency, higher cost, global LB support\n- Standard: Higher latency, lower cost, regional only\n- Set per resource (IP address or forwarding rule)"
            },
            {
                "category": "Networking",
                "front": "Packet Mirroring?",
                "back": "- Clones network traffic from VM instances for analysis\n- Mirrors ingress and/or egress traffic\n- Send to internal load balancer backed by collector VMs\n- Use cases: IDS/IPS, network forensics, compliance monitoring\n- Filter by protocol, IP range, or direction\n- Does not affect source VM performance"
            },
            {
                "category": "CDN",
                "front": "Cloud CDN: Key concepts?",
                "back": "- Content delivery network using Google's edge PoPs\n- Works with External HTTP(S) Load Balancer\n- Cache modes: USE_ORIGIN_HEADERS, CACHE_ALL_STATIC, FORCE_CACHE_ALL\n- Signed URLs and signed cookies for access control\n- Cache invalidation API for content updates\n- Reduces latency and origin server load"
            },
            {
                "category": "Hybrid",
                "front": "Network connectivity design patterns?",
                "back": "- Hub-and-spoke: Central VPC (hub) connected to project VPCs (spokes)\n- Shared VPC: Centralized network administration\n- VPC Peering: Direct VPC-to-VPC connectivity (non-transitive)\n- Cloud VPN/Interconnect: On-prem to cloud connectivity\n- NCC (Network Connectivity Center): Hub for multi-cloud/hybrid networking"
            },
            {
                "category": "IP Management",
                "front": "Private vs Public IP addressing?",
                "back": "- Internal (private) IPs: Assigned from subnet CIDR, free\n- External (public) IPs: Ephemeral (free when attached) or static (charged when idle)\n- Alias IP ranges: Assign multiple IPs to a single VM NIC\n- Private Google Access: Reach Google APIs without external IP\n- IPv6: Supported on VPCs and subnets (dual-stack)"
            },
            {
                "category": "Performance",
                "front": "Network Telemetry tools?",
                "back": "- VPC Flow Logs: IP traffic metadata\n- Firewall Rules Logging: Track rule matches\n- Packet Mirroring: Full packet capture\n- Network Intelligence Center: Topology, connectivity tests\n- Performance Dashboard: Network latency and packet loss\n- Use connectivity tests to debug routing issues"
            },
            {
                "category": "Security",
                "front": "SSL/TLS policies and certificates?",
                "back": "- Managed SSL certificates: Auto-provisioned and renewed by Google\n- Self-managed: Upload your own certificates\n- SSL policies: Control min TLS version and cipher suites\n- Certificate Manager: Large-scale certificate management\n- TLS 1.2+ recommended, TLS 1.0/1.1 deprecated"
            }
        ],
        "google-professional-cloud-database-engineer": [
            {
                "category": "Relational",
                "front": "Cloud SQL high availability setup?",
                "back": "- Regional HA: Primary + standby in different zones\n- Automatic failover to standby (60-second detection)\n- Synchronous replication for zero data loss\n- Read replicas for scaling reads (async replication)\n- Cross-region replicas for disaster recovery\n- Supports MySQL, PostgreSQL, SQL Server"
            },
            {
                "category": "Relational",
                "front": "Cloud Spanner: When and why?",
                "back": "- Globally distributed, strongly consistent relational database\n- Horizontal scaling with automatic sharding\n- 99.999% SLA (multi-region) or 99.99% (regional)\n- Supports SQL and transactions at scale\n- Use when: Global users, high write throughput, strong consistency needed\n- More expensive than Cloud SQL, justified at scale"
            },
            {
                "category": "NoSQL",
                "front": "Firestore: Native mode vs Datastore mode?",
                "back": "- Native mode: Real-time listeners, offline support, mobile/web SDK\n- Datastore mode: Server-side only, backward compatible with Datastore API\n- Cannot switch modes after database creation\n- Native: Best for mobile/web apps needing real-time sync\n- Datastore mode: Best for server-side applications\n- Both are document databases with strong consistency"
            },
            {
                "category": "NoSQL",
                "front": "Bigtable architecture and components?",
                "back": "- Wide-column NoSQL database for high throughput\n- Nodes: Compute units (min 1, linear scaling)\n- Tablets: Automatically sharded ranges of row keys\n- Column families: Group related columns\n- Compaction: Background optimization of storage\n- SSD or HDD storage (SSD for latency-sensitive workloads)"
            },
            {
                "category": "Migration",
                "front": "Database Migration Service (DMS)?",
                "back": "- Fully managed service for database migrations\n- Supports MySQL, PostgreSQL, SQL Server to Cloud SQL\n- Minimal downtime using continuous replication\n- AlloyDB and Cloud SQL as destinations\n- Handles schema conversion and data validation\n- Connectivity via VPC peering, reverse SSH, or IP allowlisting"
            },
            {
                "category": "Performance",
                "front": "Cloud SQL performance tuning?",
                "back": "- Right-size vCPUs and memory (max 96 vCPUs)\n- Use SSD storage (max 64 TB)\n- Enable query insights for slow query analysis\n- Create appropriate indexes for query patterns\n- Use connection pooling (PgBouncer, ProxySQL)\n- Read replicas to offload read traffic"
            },
            {
                "category": "Backup",
                "front": "Database backup strategies on GCP?",
                "back": "- Cloud SQL: Automated daily backups (7-day retention), on-demand backups\n- Cloud SQL: Point-in-time recovery (PITR) using binary logs/WAL\n- Spanner: Automatic versioning, on-demand and scheduled backups\n- Bigtable: Managed backups with table-level granularity\n- Firestore: Daily automatic backups, manual export to GCS"
            },
            {
                "category": "Relational",
                "front": "AlloyDB: What makes it different?",
                "back": "- PostgreSQL-compatible, fully managed database\n- Combines transactional and analytical processing\n- Up to 4x faster than standard PostgreSQL (writes)\n- Up to 100x faster for analytical queries (columnar engine)\n- 99.99% SLA with regional and cross-region replication\n- AI/ML integration with vector search support"
            },
            {
                "category": "Security",
                "front": "Database security best practices on GCP?",
                "back": "- Private IP only (no public IP unless necessary)\n- VPC Service Controls for data exfiltration prevention\n- Cloud SQL Auth Proxy for secure connections\n- IAM database authentication (PostgreSQL/MySQL)\n- Customer-managed encryption keys (CMEK)\n- Audit logging for all database operations"
            },
            {
                "category": "Design",
                "front": "Choosing the right GCP database?",
                "back": "- Relational + regional: Cloud SQL or AlloyDB\n- Relational + global: Cloud Spanner\n- Document/mobile: Firestore (Native mode)\n- Wide-column/IoT: Cloud Bigtable\n- In-memory cache: Memorystore (Redis/Memcached)\n- Key-value serverless: Firestore (Datastore mode)\n- Time-series: Bigtable or Cloud Monitoring"
            },
            {
                "category": "Scaling",
                "front": "Cloud Spanner scaling and performance?",
                "back": "- Nodes: Each provides ~10K reads/sec or ~2K writes/sec\n- Auto-scaler: Adjusts nodes based on CPU utilization\n- Interleaved tables: Co-locate parent-child rows for performance\n- Avoid hotspots: Use UUIDv4 or bit-reversed sequential keys\n- Stale reads: Read at a timestamp for lower latency\n- Multi-region configs: nam6, eur5, asia1 for global reach"
            },
            {
                "category": "Connectivity",
                "front": "Cloud SQL Auth Proxy?",
                "back": "- Secure tunnel to Cloud SQL without IP allowlisting\n- Uses IAM for authentication and authorization\n- Encrypts traffic with TLS (auto-managed certs)\n- Supports TCP and Unix socket connections\n- Run as sidecar in GKE or local proxy on VM\n- Recommended connection method for all workloads"
            },
            {
                "category": "Monitoring",
                "front": "Database monitoring and troubleshooting?",
                "back": "- Cloud SQL Insights: Query performance dashboard\n- Slow query log analysis and recommendations\n- Cloud Monitoring: CPU, memory, disk, connections metrics\n- Alerting on high replication lag or connection count\n- Bigtable Key Visualizer: Identify hotspot patterns\n- Spanner Query Statistics: Analyze query shape and cost"
            },
            {
                "category": "Optimization",
                "front": "Memorystore use cases and configuration?",
                "back": "- Redis: Session cache, leaderboards, pub/sub, Lua scripting\n- Memcached: Simple key-value caching, multi-threaded\n- Redis supports persistence and replication (HA)\n- Memcached: Volatile cache, no persistence\n- Standard tier: HA with automatic failover (Redis)\n- Basic tier: Single node, no replication"
            },
            {
                "category": "Best Practices",
                "front": "Spanner schema design best practices?",
                "back": "- Avoid monotonically increasing primary keys (causes hotspots)\n- Use UUIDv4 or bit-reversed keys for distribution\n- Interleave child tables with parent for co-located access\n- Design for access patterns, not just data model\n- Use secondary indexes sparingly (storage and write overhead)\n- Commit timestamps for ordering without hotspots"
            }
        ],
        "google-professional-machine-learning-engineer": [
            {
                "category": "ML Workflow",
                "front": "Vertex AI end-to-end ML workflow?",
                "back": "- Data prep: Vertex AI Datasets, Feature Store\n- Training: AutoML or custom training with containers\n- Evaluation: Model evaluation metrics dashboard\n- Deployment: Vertex AI Endpoints (online) or batch prediction\n- Monitoring: Model Monitoring for drift detection\n- Pipelines: Vertex AI Pipelines for MLOps automation"
            },
            {
                "category": "ML Workflow",
                "front": "AutoML vs Custom Training on Vertex AI?",
                "back": "- AutoML: No-code, Google searches best architecture\n- Custom: Full control, bring your own TensorFlow/PyTorch/XGBoost\n- AutoML: Best for tabular, image, text, video when domain knowledge is limited\n- Custom: Best when you need specific architectures or optimization\n- AutoML supports edge deployment for mobile/IoT"
            },
            {
                "category": "Feature Engineering",
                "front": "Vertex AI Feature Store?",
                "back": "- Centralized repository for ML features\n- Serves features for training and online prediction consistently\n- Prevents training-serving skew\n- Supports point-in-time lookups for historical features\n- Feature monitoring for drift detection\n- Integrates with BigQuery for offline feature computation"
            },
            {
                "category": "Data",
                "front": "Handling class imbalance in ML?",
                "back": "- Oversampling: Duplicate minority class examples (SMOTE)\n- Undersampling: Remove majority class examples\n- Class weights: Penalize misclassification of minority class more\n- Data augmentation: Create synthetic minority examples\n- Evaluation: Use precision, recall, F1, AUC-ROC instead of accuracy\n- Stratified sampling for train/test splits"
            },
            {
                "category": "Training",
                "front": "Distributed training strategies?",
                "back": "- Data parallelism: Split data across workers, each has full model\n- Model parallelism: Split model layers across workers\n- Mirrored strategy: Synchronous training on multiple GPUs\n- Parameter server: Async training with centralized parameters\n- Vertex AI handles distributed training infrastructure\n- Use when dataset or model is too large for single GPU"
            },
            {
                "category": "Evaluation",
                "front": "Key ML evaluation metrics?",
                "back": "- Accuracy: Overall correct predictions (misleading for imbalanced data)\n- Precision: True positives / (True positives + False positives)\n- Recall: True positives / (True positives + False negatives)\n- F1 Score: Harmonic mean of precision and recall\n- AUC-ROC: Model's ability to distinguish classes\n- RMSE/MAE: Regression metrics for continuous predictions"
            },
            {
                "category": "MLOps",
                "front": "Vertex AI Pipelines?",
                "back": "- Managed orchestration for ML workflows (based on KFP/TFX)\n- Define pipeline as a DAG of components\n- Components: Reusable, containerized tasks\n- Automatic lineage tracking and metadata storage\n- Scheduling: Run pipelines on cron or trigger-based\n- Compare experiments and model versions"
            },
            {
                "category": "Serving",
                "front": "Online vs Batch prediction?",
                "back": "- Online: Real-time, low-latency predictions via REST/gRPC endpoint\n- Batch: Process large datasets asynchronously\n- Online: Use for user-facing applications\n- Batch: Use for scoring large datasets, reports, recommendations\n- Vertex AI Endpoints auto-scale based on traffic\n- Batch predictions output to BigQuery or Cloud Storage"
            },
            {
                "category": "Monitoring",
                "front": "Model monitoring and drift detection?",
                "back": "- Training-serving skew: Feature distribution differs between training and serving\n- Prediction drift: Model output distribution changes over time\n- Feature drift: Input feature distributions shift\n- Vertex AI Model Monitoring: Automatic drift detection\n- Set alerting thresholds for feature and prediction drift\n- Retrain when drift exceeds acceptable bounds"
            },
            {
                "category": "Data Processing",
                "front": "TFX (TensorFlow Extended) components?",
                "back": "- ExampleGen: Data ingestion and splitting\n- StatisticsGen: Generate dataset statistics\n- SchemaGen: Infer data schema\n- ExampleValidator: Detect anomalies in data\n- Transform: Feature engineering at scale\n- Trainer: Model training\n- Evaluator: Model evaluation and validation\n- Pusher: Deploy validated models"
            },
            {
                "category": "Optimization",
                "front": "Hyperparameter tuning on Vertex AI?",
                "back": "- Vertex AI Vizier: Managed hyperparameter optimization\n- Search algorithms: Bayesian, grid search, random search\n- Early stopping: Terminate underperforming trials\n- Objective metric: What to optimize (accuracy, loss, etc.)\n- Parallel trials: Run multiple configurations simultaneously\n- Transfer learning to reduce search space"
            },
            {
                "category": "Responsible AI",
                "front": "Explainable AI on Vertex AI?",
                "back": "- Feature attributions: Which features influenced predictions most\n- Methods: Sampled Shapley, Integrated Gradients, XRAI\n- Model cards: Document model performance and limitations\n- Fairness indicators: Evaluate model across demographic groups\n- What-If Tool: Interactive model exploration\n- Required for regulatory compliance in many industries"
            },
            {
                "category": "NLP",
                "front": "NLP techniques and GCP services?",
                "back": "- Pre-trained: Natural Language API (sentiment, entity, syntax)\n- AutoML: Custom text classification and entity extraction\n- Custom: Train BERT/T5 on Vertex AI custom training\n- Embeddings: Text embeddings for semantic search\n- LLMs: Gemini/PaLM via Vertex AI for generation tasks\n- Document AI: Extract structured data from documents"
            },
            {
                "category": "Data Prep",
                "front": "Feature engineering best practices?",
                "back": "- Normalization: Scale features to same range (StandardScaler, MinMaxScaler)\n- Encoding: One-hot for categorical, embeddings for high-cardinality\n- Bucketization: Convert continuous to discrete ranges\n- Feature crosses: Combine features for non-linear relationships\n- Handle missing values: Imputation, indicator variables\n- Time features: Extract day-of-week, hour, season from timestamps"
            },
            {
                "category": "Infrastructure",
                "front": "GPU and TPU selection for ML training?",
                "back": "- GPU: NVIDIA T4 (inference), V100 (training), A100 (large models)\n- TPU: Google's custom ASICs, optimized for TensorFlow/JAX\n- TPU v4: 275 TFLOPS, best for large-scale training\n- GPU: More flexible, supports PyTorch/TF/JAX\n- TPU: Higher throughput for supported frameworks\n- Preemptible/Spot GPUs: Up to 70% cheaper for training"
            }
        ],
        "google-professional-workspace-administrator": [
            {
                "category": "User Management",
                "front": "Google Workspace user lifecycle?",
                "back": "- Provision: Admin Console, API, or Directory Sync (GCDS)\n- Assign licenses: Enterprise, Business, Frontline editions\n- Organizational Units (OUs): Control policies by group\n- Suspend: Temporarily disable account (preserves data)\n- Delete: Remove user (data can be transferred first)\n- Transfer ownership of Drive, Calendar, etc. before deletion"
            },
            {
                "category": "Security",
                "front": "Google Workspace security features?",
                "back": "- 2-Step Verification: FIDO2 keys, TOTP, push notifications\n- Context-Aware Access: Device and network conditions\n- DLP rules: Prevent sensitive data sharing in Drive/Gmail\n- Security Investigation Tool: Trace security events\n- Alert Center: Security and compliance notifications\n- Advanced Protection Program for high-value targets"
            },
            {
                "category": "Mail",
                "front": "Gmail routing and compliance?",
                "back": "- Routing rules: Default, split, dual delivery\n- Content compliance: Scan and filter based on content\n- DLP: Detect and block sensitive information\n- Email audit: Track message delivery and compliance\n- S/MIME: End-to-end encryption for email\n- Quarantine: Hold suspicious messages for admin review"
            },
            {
                "category": "Directory",
                "front": "Google Cloud Directory Sync (GCDS)?",
                "back": "- Synchronize users, groups, OUs from Active Directory/LDAP\n- One-way sync: AD/LDAP is source of truth\n- Supports attribute mapping and filtering\n- Runs on a designated sync machine (not cloud-hosted)\n- Password Sync requires separate Password Sync tool\n- Schedule sync intervals (recommended: every 1-4 hours)"
            },
            {
                "category": "Drive",
                "front": "Google Drive storage and sharing policies?",
                "back": "- Shared drives: Team-owned, membership-based access\n- External sharing: Control at domain, OU, or group level\n- Link sharing: Anyone, organization, specific people\n- DLP rules: Scan and restrict sharing of sensitive content\n- Drive labels: Classify and manage documents\n- Storage quotas: Per-user storage limits by license tier"
            },
            {
                "category": "Mobile",
                "front": "Endpoint management for mobile devices?",
                "back": "- Basic: Screen lock enforcement, remote wipe\n- Advanced: Device approval, compliance policies, app management\n- Android: Work profiles for BYOD, fully managed for corporate\n- iOS: MDM profiles with configuration policies\n- Windows: Device management via Endpoint Verification\n- Context-Aware Access integrates device trust signals"
            },
            {
                "category": "Migration",
                "front": "Workspace migration tools?",
                "back": "- Data Migration Service: Migrate email, calendar, contacts\n- Supports: Exchange, IMAP, Office 365, other Workspace\n- Migrate Drive data via Google Workspace Migrate tool\n- Parallel migration for large organizations\n- MX record cutover: Final step to receive new mail in Gmail\n- Post-migration validation: Verify data integrity"
            },
            {
                "category": "Identity",
                "front": "SSO and third-party IdP integration?",
                "back": "- SAML 2.0 SSO with external identity providers\n- Google as IdP: Other apps authenticate via Google\n- Third-party IdP: Okta, Azure AD, Ping authenticate to Google\n- OAuth 2.0 for API access and third-party app authorization\n- Control third-party app access: Allow, limited, or blocked\n- Admin can revoke OAuth tokens for all users"
            },
            {
                "category": "Compliance",
                "front": "Vault and data retention?",
                "back": "- Google Vault: eDiscovery and data retention\n- Retention rules: Hold data beyond user deletion\n- Legal holds: Preserve data for litigation\n- Search and export: Gmail, Drive, Chat, Meet recordings\n- Audit logs: Track who searched and exported what\n- Custom retention: Set by OU, date range, or terms"
            },
            {
                "category": "Monitoring",
                "front": "Admin Console reporting and alerts?",
                "back": "- Usage reports: Apps usage, user activity, device status\n- Security reports: File sharing, login attempts, password strength\n- Audit logs: Admin, Drive, Login, SAML, Groups, Mobile\n- Alert Center: Pre-configured and custom alerts\n- BigQuery export: Detailed log analysis and custom dashboards\n- Reports API for programmatic access"
            },
            {
                "category": "Collaboration",
                "front": "Google Meet admin controls?",
                "back": "- Recording: Auto-save to organizer's Drive\n- Access controls: Domain-only or allow external participants\n- Safety features: Host management, quick access, dial-in PINs\n- Quality monitoring: Meet quality tool for call diagnostics\n- Breakout rooms, Q&A, polls for engagement\n- Attendance tracking and reporting"
            },
            {
                "category": "Network",
                "front": "Workspace network requirements?",
                "back": "- Allow-list Google IP ranges for firewall\n- MX records: Point to Google mail servers\n- SPF, DKIM, DMARC: Email authentication records\n- TLS enforcement: Require encrypted email delivery\n- LDAP client: Secure LDAP for legacy app integration\n- Proxy configuration for endpoint verification"
            }
        ],
        "aws-certified-cloud-practitioner": [
            {
                "category": "Compute",
                "front": "EC2 instance types and use cases?",
                "back": "- General Purpose (T3, M5): Balanced compute, memory, networking\n- Compute Optimized (C5): High-performance processing, batch\n- Memory Optimized (R5, X1): In-memory caching, databases\n- Storage Optimized (I3, D2): High sequential read/write\n- Accelerated Computing (P3, G4): GPU for ML/graphics\n- T3 burstable: Earn credits when idle, burst when needed"
            },
            {
                "category": "Compute",
                "front": "EC2 pricing models?",
                "back": "- On-Demand: Pay by second, no commitment\n- Reserved Instances: 1-3 year commit, up to 72% savings\n- Spot Instances: Up to 90% off, can be reclaimed with 2-min warning\n- Savings Plans: Flexible commitment (compute or EC2-specific)\n- Dedicated Hosts: Physical servers for compliance\n- Dedicated Instances: Isolated hardware, per-instance billing"
            },
            {
                "category": "Storage",
                "front": "S3 storage classes?",
                "back": "- Standard: Frequently accessed, 99.99% availability\n- Intelligent-Tiering: Auto-moves between tiers based on access\n- Standard-IA: Infrequent access, lower cost, retrieval fee\n- One Zone-IA: Single AZ, 20% less than Standard-IA\n- Glacier Instant: Archive with millisecond retrieval\n- Glacier Flexible: Minutes-hours retrieval\n- Glacier Deep Archive: Cheapest, 12-48 hour retrieval"
            },
            {
                "category": "Storage",
                "front": "EBS volume types?",
                "back": "- gp3: General Purpose SSD, 3000 IOPS baseline, 125 MB/s\n- gp2: General Purpose SSD, burstable to 3000 IOPS\n- io2 Block Express: Provisioned IOPS, up to 256K IOPS\n- st1: Throughput Optimized HDD, big data workloads\n- sc1: Cold HDD, lowest cost for infrequent access\n- Boot volumes: Only gp2, gp3, io1, io2 supported"
            },
            {
                "category": "Networking",
                "front": "VPC components and concepts?",
                "back": "- VPC: Regional virtual network\n- Subnets: AZ-specific, public (with IGW route) or private\n- Internet Gateway (IGW): Allows internet access for VPC\n- NAT Gateway: Outbound internet for private subnets\n- Route Tables: Control traffic routing\n- Security Groups: Stateful, instance-level firewall\n- NACLs: Stateless, subnet-level firewall"
            },
            {
                "category": "Networking",
                "front": "Security Groups vs NACLs?",
                "back": "- Security Groups: Stateful (return traffic auto-allowed), instance-level\n- NACLs: Stateless (must allow both inbound and outbound), subnet-level\n- SG: Allow rules only (implicit deny all)\n- NACL: Allow AND deny rules, processed in order by rule number\n- Best practice: Use SGs for primary security, NACLs as extra layer"
            },
            {
                "category": "Database",
                "front": "RDS vs Aurora vs DynamoDB?",
                "back": "- RDS: Managed relational DB (MySQL, PostgreSQL, Oracle, SQL Server)\n- Aurora: AWS-optimized relational, 5x MySQL / 3x PostgreSQL performance\n- DynamoDB: Serverless NoSQL, single-digit ms latency\n- RDS: Multi-AZ for HA, read replicas for scaling\n- Aurora: Auto-scaling storage up to 128 TB, multi-master\n- DynamoDB: Auto-scaling, global tables for multi-region"
            },
            {
                "category": "HA",
                "front": "High availability patterns on AWS?",
                "back": "- Multi-AZ deployments for RDS, ElastiCache\n- Auto Scaling Groups across AZs\n- Application Load Balancer distributes traffic\n- Route 53 health checks and failover routing\n- S3 cross-region replication for data\n- Aurora Global Database for cross-region DR"
            },
            {
                "category": "Security",
                "front": "IAM best practices on AWS?",
                "back": "- Enable MFA for root account and all users\n- Use IAM roles instead of access keys\n- Principle of least privilege\n- Use AWS Organizations SCPs for guardrails\n- Rotate credentials regularly\n- Use IAM Access Analyzer to identify unintended access"
            },
            {
                "category": "Serverless",
                "front": "Lambda: Key limits and features?",
                "back": "- Max execution time: 15 minutes\n- Memory: 128 MB to 10 GB\n- Deployment package: 50 MB zipped, 250 MB unzipped\n- Concurrency: 1000 per region (adjustable)\n- Triggers: API Gateway, S3, SQS, DynamoDB Streams, EventBridge\n- Pay per invocation and duration (1ms billing)"
            },
            {
                "category": "Caching",
                "front": "ElastiCache: Redis vs Memcached?",
                "back": "- Redis: Persistence, replication, pub/sub, complex data types\n- Memcached: Multi-threaded, simple caching, no persistence\n- Redis: Supports Multi-AZ with automatic failover\n- Memcached: Supports auto-discovery of nodes\n- Redis: Best for leaderboards, sessions, real-time analytics\n- Memcached: Best for simple key-value caching at scale"
            },
            {
                "category": "Messaging",
                "front": "SQS vs SNS vs EventBridge?",
                "back": "- SQS: Queue-based, consumer pulls messages, decouples services\n- SNS: Pub/Sub, push-based fan-out to subscribers\n- EventBridge: Event bus with rules and filtering\n- SQS: At-least-once delivery (Standard) or exactly-once (FIFO)\n- SNS: Topics → Email, SMS, Lambda, SQS, HTTP endpoints\n- EventBridge: Event-driven architectures with 100+ AWS service sources"
            },
            {
                "category": "CDN",
                "front": "CloudFront: Key features?",
                "back": "- Global CDN with 400+ edge locations\n- Origins: S3, ALB, EC2, custom HTTP servers\n- Lambda@Edge: Run code at edge locations\n- Field-level encryption for sensitive data\n- Signed URLs and cookies for private content\n- Origin Access Identity (OAI): Restrict S3 access to CloudFront only"
            },
            {
                "category": "Migration",
                "front": "AWS migration services?",
                "back": "- AWS Migration Hub: Central tracking for migrations\n- Application Migration Service: Lift-and-shift servers\n- Database Migration Service (DMS): Migrate databases\n- Schema Conversion Tool (SCT): Convert schemas between engines\n- Snowball/Snowcone: Physical data transfer devices\n- DataSync: Online data transfer for files and objects"
            },
            {
                "category": "Monitoring",
                "front": "CloudWatch: Key concepts?",
                "back": "- Metrics: CPU, network, disk, custom application metrics\n- Alarms: Trigger actions based on metric thresholds\n- Logs: Centralized log management and analysis\n- Dashboards: Custom visualization of metrics\n- Events/EventBridge: React to AWS resource state changes\n- Detailed monitoring: 1-minute intervals (vs 5-min default)"
            }
        ],
        "dbt-certified-developer": dbt_cards,
        "dbt-certified-analytics-engineer": dbt_cards,
        "microsoft-azure-fundamentals": [
            {
                "category": "Cloud Concepts",
                "front": "Azure regions and availability zones?",
                "back": "- Region: Geographic area with one or more data centers\n- Availability Zone: Physically separate data center within a region\n- 60+ regions worldwide, most with 3 AZs\n- Region Pairs: Two regions paired for disaster recovery\n- Sovereign regions: US Gov, China (21Vianet)\n- Geography: Contains 2+ regions for data residency compliance"
            },
            {
                "category": "Cloud Concepts",
                "front": "IaaS vs PaaS vs SaaS on Azure?",
                "back": "- IaaS: Virtual Machines, Virtual Networks, Storage Accounts\n- PaaS: App Service, Azure SQL, Azure Functions\n- SaaS: Microsoft 365, Dynamics 365, Power Platform\n- IaaS: You manage OS, runtime, apps\n- PaaS: You manage apps and data only\n- SaaS: You manage data and access configuration only"
            },
            {
                "category": "Compute",
                "front": "Azure compute services comparison?",
                "back": "- Virtual Machines: Full IaaS, most control\n- App Service: PaaS web hosting, auto-scaling\n- Azure Functions: Serverless, event-driven, pay per execution\n- Container Instances (ACI): Serverless containers\n- Azure Kubernetes Service (AKS): Managed Kubernetes\n- Virtual Desktop: Cloud-hosted Windows desktops"
            },
            {
                "category": "Storage",
                "front": "Azure Storage account types?",
                "back": "- Blob Storage: Unstructured data (hot, cool, cold, archive tiers)\n- File Storage: Managed file shares (SMB/NFS protocol)\n- Queue Storage: Message queuing between components\n- Table Storage: NoSQL key-value store\n- Disk Storage: Managed disks for VMs (Standard HDD/SSD, Premium SSD, Ultra)\n- Data Lake Storage Gen2: Hierarchical namespace for analytics"
            },
            {
                "category": "Storage",
                "front": "Azure Blob Storage access tiers?",
                "back": "- Hot: Frequently accessed, highest storage cost, lowest access cost\n- Cool: Infrequently accessed, 30-day minimum, lower storage cost\n- Cold: Rarely accessed, 90-day minimum\n- Archive: Offline, 180-day minimum, hours to rehydrate\n- Lifecycle management policies auto-transition between tiers\n- Set at account level (default) or blob level"
            },
            {
                "category": "Networking",
                "front": "Azure networking fundamentals?",
                "back": "- Virtual Network (VNet): Isolated network in Azure (regional)\n- Subnets: Segments within a VNet\n- Network Security Groups (NSGs): Filter traffic by rules\n- Azure Firewall: Managed network security service\n- VPN Gateway: Encrypted connection to on-premises\n- ExpressRoute: Private, dedicated connection to Azure"
            },
            {
                "category": "Identity",
                "front": "Microsoft Entra ID (Azure AD) basics?",
                "back": "- Cloud-based identity and access management service\n- SSO to thousands of SaaS applications\n- Multi-Factor Authentication (MFA)\n- Conditional Access: Policy-based access control\n- B2B: External user collaboration\n- B2C: Customer identity management\n- Replaces Azure Active Directory branding"
            },
            {
                "category": "Security",
                "front": "Azure security tools and services?",
                "back": "- Microsoft Defender for Cloud: Security posture management\n- Azure Sentinel: Cloud-native SIEM and SOAR\n- Key Vault: Manage secrets, keys, and certificates\n- DDoS Protection: Standard tier for enhanced protection\n- Azure Information Protection: Classify and protect data\n- Microsoft Secure Score: Security improvement recommendations"
            },
            {
                "category": "Governance",
                "front": "Azure governance hierarchy?",
                "back": "- Management Groups: Organize subscriptions\n- Subscriptions: Billing and access boundary\n- Resource Groups: Logical container for resources\n- Resources: Individual services (VMs, DBs, etc.)\n- RBAC: Role-based access control at any level\n- Azure Policy: Enforce organizational standards\n- Blueprints: Repeatable environment templates"
            },
            {
                "category": "Cost",
                "front": "Azure cost management tools?",
                "back": "- Pricing Calculator: Estimate costs before deployment\n- TCO Calculator: Compare on-prem vs Azure costs\n- Cost Management: Monitor and analyze spending\n- Advisor: Cost optimization recommendations\n- Reserved Instances: 1-3 year commit for savings\n- Spot VMs: Unused capacity at deep discounts\n- Azure Hybrid Benefit: Use existing Windows/SQL licenses"
            },
            {
                "category": "Compliance",
                "front": "Azure compliance and trust?",
                "back": "- Trust Center: Compliance documentation hub\n- Service Trust Portal: Audit reports and certifications\n- 100+ compliance offerings (GDPR, HIPAA, PCI-DSS, SOC)\n- Azure compliance documentation: Region-specific requirements\n- Compliance Manager: Track compliance progress\n- Data residency: Control where data is stored"
            },
            {
                "category": "Management",
                "front": "Azure management tools?",
                "back": "- Azure Portal: Web-based GUI\n- Azure CLI: Cross-platform command line (bash-style)\n- Azure PowerShell: Windows PowerShell cmdlets\n- Azure Cloud Shell: Browser-based CLI (Bash or PowerShell)\n- Azure Mobile App: Monitor and manage on-the-go\n- ARM Templates / Bicep: Infrastructure as Code\n- Azure Arc: Manage multi-cloud and on-prem resources"
            },
            {
                "category": "Database",
                "front": "Azure database services?",
                "back": "- Azure SQL Database: Managed SQL Server (PaaS)\n- Azure SQL Managed Instance: Near 100% SQL Server compatibility\n- Cosmos DB: Globally distributed, multi-model NoSQL\n- Azure Database for MySQL/PostgreSQL: Managed open-source DBs\n- Azure Cache for Redis: In-memory caching\n- Cosmos DB: Single-digit ms latency, 99.999% availability"
            },
            {
                "category": "AI",
                "front": "Azure AI and ML services?",
                "back": "- Azure AI Services: Pre-built APIs (vision, speech, language)\n- Azure OpenAI Service: GPT-4, DALL-E, Whisper access\n- Azure Machine Learning: End-to-end ML platform\n- Azure Bot Service: Build conversational AI bots\n- Cognitive Search: AI-powered search with indexing\n- Form Recognizer: Extract data from documents"
            },
            {
                "category": "Monitoring",
                "front": "Azure monitoring and support?",
                "back": "- Azure Monitor: Metrics, logs, alerts, diagnostics\n- Application Insights: App performance monitoring (APM)\n- Log Analytics: Query and analyze log data (KQL)\n- Service Health: Track Azure service incidents\n- Azure Advisor: Best practice recommendations\n- Support plans: Basic (free), Developer, Standard, Professional Direct"
            }
        ]
    }
    return flashcards.get(cert_id, [])
