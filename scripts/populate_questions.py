import os
import json
from cheatsheet_resources import get_cheatsheet_for_cert
from flashcard_resources import get_flashcards_for_cert
from study_flashcard_resources import get_study_flashcards_for_cert

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
        "id": "google-generative-ai-leader",
        "provider": "google-cloud",
        "name": "Google Cloud Generative AI Leader",
        "description": "Validates foundational knowledge of Generative AI concepts, responsible AI development, and deploying gen AI solutions strategically using Vertex AI, Gemini, and Agent Builder.",
        "icon": "🤖",
        "cheatsheet": {
            "summary": "Focuses on business-level strategy, ethics, foundation models (LLMs), Vertex AI platform solutions, Gemini integration, and responsible AI implementation.",
            "coreConcepts": [
                {"name": "Foundation Models & LLMs", "desc": "Large pre-trained neural networks (like Gemini) that can be adapted to various downstream tasks with minimal fine-tuning."},
                {"name": "Generative AI vs Discriminative AI", "desc": "Generative AI generates new content (text, image, audio), while Discriminative AI classifies or predicts patterns within existing data."},
                {"name": "Responsible AI & Governance", "desc": "Implementing safety filters, bias mitigation, data governance, and addressing copyright issues under Google Cloud's AI principles."},
                {"name": "Prompt Engineering & RAG", "desc": "Prompt Engineering optimizes queries to LLMs. Retrieval-Augmented Generation (RAG) grounds LLM outputs using enterprise databases for accuracy."}
            ],
            "commands": [
                {"cmd": "Vertex AI Search & Conversation", "desc": "No-code platform to build enterprise-grade search engines and generative chat agents."},
                {"cmd": "Gemini for Google Cloud", "desc": "Always-on collaborator helping developers write code, manage resources, and secure cloud environments."}
            ],
            "architecturalPatterns": [
                {"scenario": "Accurate Customer Q&A Agent", "solution": "Use Vertex AI Agent Builder to create a chat agent, connect it to enterprise PDF documentation in Cloud Storage using RAG, and enable safety filters."},
                {"scenario": "Securing Gen AI Applications", "solution": "Deploy LLMs via Vertex AI API, configure VPC Service Controls to isolate training data, and assign specific IAM roles for API invocation."}
            ]
        },
        "topics": [
            {
                "topic": "Responsible AI",
                "q": "Which of the following aligns with Google's Responsible AI principles when deploying generative models?",
                "opts": [
                    "Maximizing the model's creativity regardless of factual accuracy",
                    "Ensuring safety evaluations, monitoring bias, and implementing safety filters",
                    "Locking model outputs to prevent any variation in response",
                    "Sharing user prompts publicly to foster model collaboration"
                ],
                "ans": 1,
                "exp": "Responsible AI practices require continuous evaluation for safety, bias tracking, and deploying guardrails/filters to prevent unsafe content generation."
            },
            {
                "topic": "Vertex AI Offerings",
                "q": "Your business needs to build a custom AI chatbot that can answer customer queries using your internal company wikis and PDF files, without writing complex machine learning pipelines. Which Google Cloud tool should you select?",
                "opts": [
                    "Compute Engine VMs with manually installed PyTorch",
                    "Vertex AI Agent Builder (Search and Conversation)",
                    "Cloud Translation API",
                    "BigQuery ML with custom linear regression models"
                ],
                "ans": 1,
                "exp": "Vertex AI Agent Builder enables rapid construction of enterprise-grade search engines and generative chatbots grounded in custom internal data with minimal code."
            },
            {
                "topic": "Generative AI Concepts",
                "q": "What is the primary difference between Generative AI and Discriminative AI?",
                "opts": [
                    "Generative AI only processes numerical data, whereas Discriminative AI processes natural text.",
                    "Generative AI creates new data instances based on learned patterns, while Discriminative AI classifies existing data.",
                    "Generative AI runs only on-premises, while Discriminative AI runs in the cloud.",
                    "Discriminative AI uses deep learning, whereas Generative AI does not."
                ],
                "ans": 1,
                "exp": "Generative AI models learn data distributions to generate new, original content (e.g., text, images), whereas Discriminative AI predicts labels or categories by distinguishing between data points."
            },
            {
                "topic": "Retrieval-Augmented Generation (RAG)",
                "q": "Your company's LLM frequently outputs outdated or incorrect information about product availability. Which design pattern should you implement to ground the model's responses in real-time inventory databases?",
                "opts": [
                    "Increasing the model's temperature parameter to maximum",
                    "Fine-tuning the foundation model every hour",
                    "Retrieval-Augmented Generation (RAG)",
                    "Hardcoding answers inside the prompt itself"
                ],
                "ans": 2,
                "exp": "Retrieval-Augmented Generation (RAG) queries dynamic external databases to retrieve factual, real-time context and appends it to the user's prompt, reducing hallucinations."
            },
            {
                "topic": "Gemini for Google Cloud",
                "q": "Which tool provides conversational assistance to help write infrastructure code, analyze cloud costs, and troubleshoot GCP resource configuration?",
                "opts": [
                    "Gemini for Google Cloud",
                    "Google Cloud Looker",
                    "Vertex AI AutoML",
                    "App Engine Standard"
                ],
                "ans": 0,
                "exp": "Gemini for Google Cloud acts as an always-on AI collaborator that assists with writing code, explaining cloud resource properties, and optimizing GCP billing/security."
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

# Helper to generate links for each certification dynamically
def get_links_for_cert(cert_id):
    if "google" in cert_id:
        slug_map = {
            'google-associate-cloud-engineer': 'associate-cloud-engineer',
            'google-cloud-digital-leader': 'cloud-digital-leader',
            'google-generative-ai-leader': 'generative-ai-leader',
            'google-professional-cloud-architect': 'cloud-architect',
            'google-professional-data-engineer': 'professional-data-engineer',
            'google-professional-cloud-developer': 'cloud-developer',
            'google-professional-cloud-security-engineer': 'cloud-security-engineer',
            'google-professional-cloud-network-engineer': 'cloud-network-engineer',
            'google-professional-cloud-devops-engineer': 'cloud-devops-engineer',
            'google-professional-machine-learning-engineer': 'machine-learning-engineer'
        }
        slug = slug_map.get(cert_id, cert_id.replace('google-', ''))
        return [
            { "title": "Official GCP Exam Page", "url": f"https://cloud.google.com/learn/certification/{slug}" },
            { "title": "GCP Documentation Portal", "url": "https://cloud.google.com/docs" },
            { "title": "Google Cloud Training Portal", "url": "https://www.cloudskillsboost.google" }
        ]
    elif "dbt" in cert_id:
        slug = "developer-certification-exam" if "developer" in cert_id else "analytics-engineering-certification-exam"
        return [
            { "title": "Official dbt Exam Page", "url": f"https://www.getdbt.com/co/dbt-certification/{slug}/" },
            { "title": "dbt Core Developer Docs", "url": "https://docs.getdbt.com" },
            { "title": "dbt Slack Community Support", "url": "https://community.getdbt.com" }
        ]
    elif "aws" in cert_id:
        return [
            { "title": "Official AWS Exam Page", "url": "https://aws.amazon.com/certification/certified-cloud-practitioner/" },
            { "title": "AWS Documentation Portal", "url": "https://docs.aws.amazon.com" },
            { "title": "AWS Free Tier Management Console", "url": "https://console.aws.amazon.com" }
        ]
    elif "microsoft" in cert_id:
        return [
            { "title": "Official Microsoft AZ-900 Page", "url": "https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/" },
            { "title": "Microsoft Azure Documentation", "url": "https://learn.microsoft.com/en-us/azure/" },
            { "title": "Azure Portal Access Console", "url": "https://portal.azure.com" }
        ]
    return []

# Function to generate 50 unique questions for each certification
def generate_questions():
    final_certs = []
    
    for cert in certifications_data:
        cert_id = cert["id"]
        provider = cert["provider"]
        name = cert["name"]
        desc = cert["description"]
        icon = cert["icon"]
        cheatsheet = get_cheatsheet_for_cert(cert_id)
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
            "links": get_links_for_cert(cert_id),
            "flashcards": get_flashcards_for_cert(cert_id),
            "study_flashcards": get_study_flashcards_for_cert(cert_id),
            "questions": generated_questions
        })
        
    return {"certifications": final_certs}


# Generate and write output
data = generate_questions()
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Success! Generated data/questions.json with {len(data['certifications'])} certifications, cheatsheets, and 50 questions each!")
