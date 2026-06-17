# Detailed Flashcard Resources based on Official Exam Guide Checklists

def get_flashcards_for_cert(cert_id):
    flashcards = {
        "google-associate-cloud-engineer": [
            {
                "category": "Domain 1: Set up Cloud Environment",
                "front": "Setting up a cloud solution environment",
                "back": "- Create and configure GCP projects and billing accounts\n- Manage IAM resource bindings and user groups\n- Configure Cloud Logging and Monitoring workspaces\n- Install and initialize the Google Cloud SDK (gcloud CLI)"
            },
            {
                "category": "Domain 2: Plan and Configure",
                "front": "Planning and configuring a cloud solution",
                "back": "- Estimate resource costs using the GCP Pricing Calculator\n- Select VM configurations (vCPUs, RAM, local vs persistent disks)\n- Plan and configure regional VPC networks and subnets\n- Choose database solutions (SQL vs Spanner vs Firestore) based on load"
            },
            {
                "category": "Domain 3: Deploy and Implement",
                "front": "Deploying and implementing a cloud solution",
                "back": "- Deploy Compute Engine VMs and Managed Instance Groups (MIGs)\n- Deploy GKE clusters, configure pods, and expose load-balanced services\n- Deploy App Engine and Cloud Run serverless applications\n- Configure VPC firewall rules and target network tags"
            },
            {
                "category": "Domain 4: Operation and Monitoring",
                "front": "Ensuring successful operation of a cloud solution",
                "back": "- Manage Compute Engine VM lifecycles and disk snapshots\n- Perform GKE cluster upgrades and configure node autoscaling\n- Establish Cloud Storage lifecycle rules and uniform bucket-level permissions\n- Monitor system performance metrics and set up alerts"
            },
            {
                "category": "Domain 5: Access and Security",
                "front": "Configuring access and security",
                "back": "- Apply the Principle of Least Privilege using predefined IAM roles\n- Create and assign Service Accounts to VM instances securely\n- Inspect audit trails using Cloud Logging filters\n- Configure VPC firewall rules and private subnet routes"
            }
        ],
        "google-cloud-digital-leader": [
            {
                "category": "Domain 1: Transformation",
                "front": "Digital Transformation with Google Cloud",
                "back": "- Shift from Capital Expenditure (CapEx) to Operational Expenditure (OpEx)\n- Understand cloud types: Public, Private, Hybrid, and Multi-cloud\n- Define database modernization, serverless benefits, and API strategies\n- Calculate Total Cost of Ownership (TCO) and ROI business value models"
            },
            {
                "category": "Domain 2: Innovation with Data",
                "front": "Innovating with Data in the Cloud",
                "back": "- Classify unstructured vs structured vs semi-structured data\n- Select storage categories: Object, File, Block, Relational, and NoSQL\n- Understand analytics: Data lakes, data warehouses, and streaming pipelines\n- Identify business use cases for BigQuery, Looker, and Pub/Sub"
            },
            {
                "category": "Domain 3: Modernization",
                "front": "Infrastructure and Application Modernization",
                "back": "- Match compute platforms (VMs, Containers, Serverless) to workloads\n- Understand serverless scaling benefits and cold start concepts\n- Evaluate hybrid network pathways (Cloud VPN vs Interconnect)\n- Plan migration paths: Lift-and-shift, re-platforming, and refactoring"
            },
            {
                "category": "Domain 4: Security & SRE",
                "front": "Google Cloud Security and Operations",
                "back": "- Differentiate between security of the cloud vs in the cloud (Shared Responsibility)\n- Enforce access controls using the Cloud IAM hierarchy\n- Enforce network defenses: firewalls, DDoS protection, and WAF\n- Define SRE principles, SLAs, SLOs, and logging metrics"
            }
        ],
        "google-generative-ai-leader": [
            {
                "category": "Domain 1: Gen AI Basics",
                "front": "Generative AI Fundamentals",
                "back": "- Differentiate Generative AI from Discriminative AI models\n- Understand Large Language Models (LLMs) and Foundation Models\n- Define model parameters: tokens, context windows, and temperatures\n- Identify the causes of hallucinations and mitigation methods"
            },
            {
                "category": "Domain 2: Business Cases",
                "front": "Strategic Business Case Identification",
                "back": "- Assess business workflows suitable for Gen AI integrations\n- Identify common use cases: summarization, search, copywriting, code helpers\n- Structure ROI calculations for enterprise AI projects\n- Build build-vs-buy decisions for foundational LLMs"
            },
            {
                "category": "Domain 3: Vertex AI",
                "front": "Vertex AI Enterprise Tooling",
                "back": "- Deploy Vertex AI Studio for rapid prompt design and prototyping\n- Ground models using Vertex AI Agent Builder (Search & Conversation)\n- Utilize Model Garden for open-source model evaluations\n- Understand Gemini for Google Cloud operations workflows"
            },
            {
                "category": "Domain 4: Prompting & RAG",
                "front": "Grounding, Prompting, and RAG",
                "back": "- Structure prompt engineering techniques (Few-Shot, Chain-of-Thought)\n- Design Retrieval-Augmented Generation (RAG) using external databases\n- Secure vector database mappings and embeddings\n- Optimize response accuracy with real-time grounding sources"
            },
            {
                "category": "Domain 5: Ethics & Governance",
                "front": "Responsible AI & Governance",
                "back": "- Apply Google's Responsible AI Principles in software designs\n- Configure safety filters and toxicity thresholds on LLM APIs\n- Manage copyright protections and corporate data governance policies\n- Monitor model drift, bias, and output safety indicators over time"
            }
        ],
        "google-professional-cloud-architect": [
            {
                "category": "Domain 1: Architecture Design",
                "front": "Designing a Solution Infrastructure Architecture",
                "back": "- Map business objectives to highly available, multi-region technical targets\n- Design global load balancing and DNS routing configurations\n- Architect robust disaster recovery strategies (minimizing RTO/RPO)\n- Select database and storage solutions matching capacity plans"
            },
            {
                "category": "Domain 2: Security & Compliance",
                "front": "Designing for Security and Compliance",
                "back": "- Enforce centralized IAM controls and resource organizational rules\n- Define network perimeters using VPC Service Controls\n- Design data encryption strategies (managed CMEK vs supplying CSEK keys)\n- Align systems to regulations (HIPAA, GDPR, PCI-DSS) via logging"
            },
            {
                "category": "Domain 3: Scale & Reliability",
                "front": "Designing for Reliability and Scale",
                "back": "- Implement autoscaling rules for Compute Engine MIGs and GKE\n- Configure multi-region active-active failover mechanisms\n- Design caching strategies using Cloud Memorystore (Redis)\n- Establish decoupled event pipelines (Pub/Sub + Dataflow)"
            },
            {
                "category": "Domain 4: Network Architecture",
                "front": "Analyzing and Optimizing Network Operations",
                "back": "- Design hybrid network pathways (HA VPN vs Dedicated Interconnect)\n- Implement VPC network configurations: subnetting, Peering, Shared VPC\n- Optimize latency using Cloud CDN edge caches\n- Enforce firewall rules and private access configurations"
            }
        ],
        "google-professional-data-engineer": [
            {
                "category": "Domain 1: Pipeline Design",
                "front": "Designing Data Processing Systems",
                "back": "- Choose storage solutions (BigQuery, Bigtable, Cloud Storage)\n- Design pipeline schemas and structures (batch vs stream)\n- Plan infrastructure scaling and workflow pipelines\n- Configure data archiving and retention policies"
            },
            {
                "category": "Domain 2: Building Pipelines",
                "front": "Building and Operationalizing Data Pipelines",
                "back": "- Ingest data streams using Pub/Sub event brokers\n- Code data transformations inside Cloud Dataflow (Apache Beam)\n- Orchestrate daily data workflows using Cloud Composer (Airflow)\n- Migrate legacy Hadoop/Spark jobs to Cloud Dataproc"
            },
            {
                "category": "Domain 3: Model Operationalization",
                "front": "Machine Learning and Analytics",
                "back": "- Query data warehouses using BigQuery SQL commands\n- Train machine learning models directly in SQL via BigQuery ML (BQML)\n- Deploy custom ML models on Vertex AI endpoints\n- Anonymize and redact patient data using Cloud DLP API scans"
            },
            {
                "category": "Domain 4: Data Quality & Governance",
                "front": "Ensuring Data Quality and Reliability",
                "back": "- Monitor pipelines for bottlenecks using Cloud Monitoring\n- Test data outputs for accuracy and schema conformance\n- Manage data access controls with column-level IAM tags\n- Troubleshoot workflow step failures and retry pipelines"
            }
        ],
        "google-professional-cloud-developer": [
            {
                "category": "Domain 1: Cloud-Native Design",
                "front": "Designing Cloud-Native Applications",
                "back": "- Build applications using serverless runtimes (Cloud Run, Functions)\n- Secure APIs with API Gateway and authentication tokens\n- Configure containerized microservices in GKE clusters\n- Manage session state using Cloud Memorystore (Redis) caching"
            },
            {
                "category": "Domain 2: CI/CD Build",
                "front": "Building and Deploying Applications",
                "back": "- Author build steps in Cloud Build (cloudbuild.yaml)\n- Store container images in Artifact Registry\n- Deploy applications with Cloud Deploy canary rollouts\n- Inject credentials securely via Secret Manager"
            },
            {
                "category": "Domain 3: Observability",
                "front": "Monitoring and Troubleshooting",
                "back": "- Trace request latencies across services using Cloud Trace\n- Profile code resource usage with Cloud Profiler\n- Review application logs in Cloud Logging\n- Set up error reporting alerts for runtime exceptions"
            }
        ],
        "google-professional-cloud-security-engineer": [
            {
                "category": "Domain 1: Identity & Access",
                "front": "Identity and Access Management",
                "back": "- Enforce centralized IAM policies using Resource Hierarchy\n- Authenticate GKE pods safely with Workload Identity\n- Configure Cloud Identity directory syncs and user groups\n- Set up Conditional Access and IAP access controls"
            },
            {
                "category": "Domain 2: Data Protection",
                "front": "Securing Data and Applications",
                "back": "- Manage encryption keys using Customer-Managed Keys (CMEK) in KMS\n- Establish project security perimeters via VPC Service Controls\n- Redact sensitive database records using Cloud DLP API scans\n- Secure cloud storage objects with retention locks"
            },
            {
                "category": "Domain 3: Network Security",
                "front": "Configuring Network Defenses",
                "back": "- Mitigate web attacks (SQL injection) via Cloud Armor WAF rules\n- Restrict VM traffic using network tags and Firewall rules\n- Set up secure remote management via IAP TCP forwarding\n- Enable DDoS protections on HTTP(S) Load Balancers"
            }
        ],
        "google-professional-cloud-network-engineer": [
            {
                "category": "Domain 1: VPC Architecture",
                "front": "VPC Design and Implementation",
                "back": "- Plan custom subnet allocations across multi-region networks\n- Configure Shared VPCs to share networks with service projects\n- Establish private project connections with VPC Network Peering\n- Enable Private Google Access for VMs in internal subnets"
            },
            {
                "category": "Domain 2: Hybrid Networks",
                "front": "Configuring Hybrid Connectivity",
                "back": "- Deploy Dedicated Interconnect direct physical links\n- Set up Partner Interconnect routed private circuits\n- Configure HA VPN dual tunnels for 99.99% availability\n- Exchange network paths dynamically using BGP on Cloud Router"
            },
            {
                "category": "Domain 3: Load Balancing & DNS",
                "front": "Routing and Load Balancing",
                "back": "- Deploy Global HTTP(S) Load Balancer for multi-region backends\n- Resolve domains across peered VPCs using private Cloud DNS zones\n- Cache static files at edge locations with Cloud CDN\n- Configure Cloud DNS forwarding zones for hybrid name resolution"
            }
        ],
        "google-professional-cloud-devops-engineer": [
            {
                "category": "Domain 1: SRE Metrics",
                "front": "Site Reliability Engineering Principles",
                "back": "- Define Service Level Indicators (SLIs) for key services\n- Set Service Level Objectives (SLOs) to measure target availability\n- Manage Error Budgets (100% - SLO) to balance speed and safety\n- Lead blameless post-mortems for production outages"
            },
            {
                "category": "Domain 2: CI/CD Automation",
                "front": "CI/CD and Release Automation",
                "back": "- Automate packaging using Cloud Build docker commands\n- Provision resources programmatically via Terraform IaC state files\n- Deploy software with Cloud Deploy canary rollouts\n- Store packages securely in Artifact Registry"
            },
            {
                "category": "Domain 3: Operations",
                "front": "Observability and Operations",
                "back": "- Create dashboards and Alerting policies in Cloud Monitoring\n- Export log files via Log Sinks to BigQuery\n- Profile code latency with Cloud Profiler\n- Route logs to Cloud Storage buckets for compliance archiving"
            }
        ],
        "google-professional-machine-learning-engineer": [
            {
                "category": "Domain 1: Model Design",
                "front": "ML Architecture Design",
                "back": "- Select GCP ML services (AutoML vs Custom Vertex AI jobs)\n- Choose compute types (CPUs, GPUs, TPUs) for training\n- Plan data ingestion pipelines from BigQuery\n- Structure feature sharing with Vertex AI Feature Store"
            },
            {
                "category": "Domain 2: Model Training",
                "front": "Model Development and Tuning",
                "back": "- Package code in custom containers for Vertex AI custom training\n- Scale training using distributed clusters\n- Search hyperparameters using Vertex AI Vizier jobs\n- Manage training experiments in Vertex AI Pipelines (Kubeflow)"
            },
            {
                "category": "Domain 3: MLOps",
                "front": "MLOps and Model serving",
                "back": "- Deploy model artifacts to Vertex AI endpoints for online predictions\n- Run batch prediction jobs for high-volume logs\n- Monitor endpoints for training-serving data skew\n- Detect feature distribution drift over time"
            }
        ],
        "dbt-certified-developer": [
            {
                "category": "Domain 1: dbt Jinja",
                "front": "Jinja Scripting and Macro Creation",
                "back": "- Write dynamic SQL query files using Jinja loops and conditional blocks\n- Author reusable macros in the macros/ folder\n- Dispatch query structures dynamically based on database adapters\n- Leverage env variables inside dbt project config files"
            },
            {
                "category": "Domain 2: Package Management",
                "front": "Installing and managing packages",
                "back": "- Declare external package dependencies inside packages.yml\n- Download packages (e.g. dbt_utils) using 'dbt deps'\n- Override packages default macros with custom definitions\n- Leverage package-defined data tests and schemas"
            },
            {
                "category": "Domain 3: Slim CI/CD",
                "front": "Slim CI deployments in dbt Cloud",
                "back": "- Run only modified models using '--select state:modified+'\n- Defer unchanged models to production manifest.json artifact targets\n- Configure automated PR checks in dbt Cloud jobs\n- Run data tests in CI against scratch database schemas"
            },
            {
                "category": "Domain 4: Performance Tuning",
                "front": "Performance optimization in Warehouses",
                "back": "- Configure model clustering and sorting in dbt config blocks\n- Configure BigQuery partition strategies in models yml\n- Optimize table structures with dbt incremental materializations\n- Monitor model runtimes using catalog manifest artifacts"
            }
        ],
        "dbt-certified-analytics-engineer": [
            {
                "category": "Domain 1: Modeling core",
                "front": "dbt project modeling workflow",
                "back": "- Define data warehouse layers: staging, intermediate, and marts\n- Setup dbt sources using source() to isolate raw data references\n- Build DAG dependencies using ref() to direct execution sequences\n- Configure model materializations: views, tables, and CTEs"
            },
            {
                "category": "Domain 2: Materializations",
                "front": "Incremental and Ephemeral configurations",
                "back": "- Configure incremental materializations to append recent rows only\n- Filter incremental runs using Jinja 'is_incremental()' block\n- Nest models as ephemeral CTEs to avoid creating physical views\n- Troubleshoot full-refresh runs when database schemas update"
            },
            {
                "category": "Domain 3: Data Quality",
                "front": "Schema and Custom Data testing",
                "back": "- Configure schema tests (unique, not_null, accepted_values, relationships)\n- Write custom data tests in tests/ returning failed rows\n- Build project documentation descriptions in yml schema files\n- Generate docs locally using 'dbt docs generate'"
            },
            {
                "category": "Domain 4: Snapshots",
                "front": "Capturing historical state changes",
                "back": "- Implement dbt snapshots in the snapshots/ folder\n- Configure snapshots to track SCD Type 2 changes over time\n- Define check strategies (timestamp vs check_cols)\n- Query snapshot tables for historical time-range analysis"
            }
        ],
        "aws-certified-cloud-practitioner": [
            {
                "category": "Domain 1: Global Infrastructure",
                "front": "AWS Global Infrastructure",
                "back": "- AWS Regions: geographical clusters of isolated Availability Zones\n- Availability Zones: physically distinct datacenters within a region\n- Edge Locations: caching endpoints for CloudFront CDN\n- AWS Local Zones: run latency-sensitive apps close to users"
            },
            {
                "category": "Domain 2: Core Services",
                "front": "Compute, Storage, and Databases",
                "back": "- Compute: EC2 (VMs), AWS Lambda (serverless), ECS/EKS (containers)\n- Storage: Amazon S3 (objects), EBS (disks), EFS (shared network files)\n- Databases: RDS (managed SQL), DynamoDB (NoSQL document), Aurora (PaaS)"
            },
            {
                "category": "Domain 3: IAM Security",
                "front": "IAM and Shared Responsibility",
                "back": "- AWS managers security OF the cloud (physical centers, network)\n- Customer manages security IN the cloud (IAM users, firewalls, data)\n- Enforce password policies and MFA in AWS IAM console\n- Delegate access securely using IAM Roles"
            },
            {
                "category": "Domain 4: Billing & Cost",
                "front": "Billing, Pricing, and Cost Management",
                "back": "- AWS Cost Explorer: analyze historical costs and usage patterns\n- AWS Budgets: configure custom budget spend alert notifications\n- AWS Organizations: consolidate billing across multiple accounts\n- Pricing options: Reserved Instances, Savings Plans, and Spot instances"
            }
        ],
        "microsoft-azure-fundamentals": [
            {
                "category": "Domain 1: Architecture Core",
                "front": "Azure Regional Architecture",
                "back": "- Azure Regions: geographical areas containing datacenters\n- Availability Zones: physically separate datacenters inside a region\n- Azure Region Pairs: direct cross-region DR failover mappings\n- Azure Subscriptions: logical billing boundary for cloud resources"
            },
            {
                "category": "Domain 2: Compute & Storage",
                "front": "Azure Compute and Storage Services",
                "back": "- Compute: Azure VMs (IaaS), App Service (PaaS), AKS (containers)\n- Storage: Blob storage (objects), Azure Files (network), Disk storage\n- Network: Virtual Networks (VNets), ExpressRoute (private Interconnect)"
            },
            {
                "category": "Domain 3: Microsoft Entra ID",
                "front": "Azure Identity, Access, and Security",
                "back": "- Microsoft Entra ID: central identity and directory service\n- Role-Based Access Control (RBAC): assign resource permissions\n- Conditional Access: MFA policies based on user login location\n- Microsoft Defender for Cloud: unified security management"
            },
            {
                "category": "Domain 4: Governance",
                "front": "Azure Governance and Management",
                "back": "- Azure Policies: enforce configuration compliance standards\n- Azure Resource Manager (ARM): deploy Bicep/ARM templates\n- Resource Locks: prevent critical resource deletions (CannotDelete)\n- Azure Service Health: dashboard for system outage alerts"
            }
        ]
    }
    return flashcards.get(cert_id, [
        {
            "category": "Overview Objectives",
            "front": "General Certification Objectives",
            "back": "Review official exam guides to identify specific domain objectives."
        }
    ])
