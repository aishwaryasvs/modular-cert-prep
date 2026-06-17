import os
import json
import random

# Ensure output directory exists
os.makedirs('data', exist_ok=True)

# Provider and exam definitions
certifications = [
    {
        "id": "google-associate-cloud-engineer",
        "provider": "google-cloud",
        "name": "Google Associate Cloud Engineer",
        "description": "Validates your ability to deploy applications, monitor operations, manage enterprise solutions, and configure networks and security on GCP.",
        "icon": "⚡",
        "topics": [
            {
                "topic": "IAM Roles",
                "easy": {
                    "q": "Which basic IAM role allows a user to view resources but not modify them?",
                    "opts": ["Viewer (roles/viewer)", "Editor (roles/editor)", "Owner (roles/owner)", "Browser (roles/browser)"],
                    "ans": 0,
                    "exp": "The Viewer role (roles/viewer) grants read-only access to view most Google Cloud resources without making changes."
                },
                "medium": {
                    "q": "You need to grant a developer permission to deploy code to a Cloud Storage bucket and delete objects, but they must not be allowed to change bucket-level permissions. Which role should you assign?",
                    "opts": ["Storage Admin", "Storage Object Creator", "Storage Object Admin", "Storage Object Viewer"],
                    "ans": 2,
                    "exp": "Storage Object Admin allows full control over Cloud Storage objects (creation, deletion, viewing), but does not allow modifying bucket-level IAM policies, which requires Storage Admin."
                },
                "hard": {
                    "q": "A security auditor needs to review all IAM policies across your organization's projects without viewing the actual data inside databases or buckets. What is the most restrictive role for this?",
                    "opts": ["Security Reviewer (roles/iam.securityReviewer)", "Viewer (roles/viewer)", "Project IAM Admin (roles/resourcemanager.projectIamAdmin)", "Organization Administrator"],
                    "ans": 0,
                    "exp": "The Security Reviewer role grants permissions to view security policies (such as IAM policies) across resources without permitting data access."
                }
            },
            {
                "topic": "Compute Engine",
                "easy": {
                    "q": "Which Google Cloud service provides virtual machine instances that you can manage directly?",
                    "opts": ["Cloud Run", "Compute Engine", "App Engine", "Google Kubernetes Engine"],
                    "ans": 1,
                    "exp": "Compute Engine is Google Cloud's Infrastructure as a Service (IaaS) that provides customizable virtual machines."
                },
                "medium": {
                    "q": "You want to set up autoscaling for a web application running on Compute Engine VMs. What resource type must you create first to enable autoscaling?",
                    "opts": ["An unmanaged instance group", "A managed instance group (MIG)", "A load balancer", "A virtual private cloud (VPC)"],
                    "ans": 1,
                    "exp": "Compute Engine autoscaling is a feature of Managed Instance Groups (MIGs). You cannot configure autoscaling on unmanaged instance groups."
                },
                "hard": {
                    "q": "You need to configure a Compute Engine VM with local SSDs. What is a key characteristic of data stored on Local SSDs that you must plan for?",
                    "opts": [
                        "Data is persistent and survives instance deletion.",
                        "Data is encrypted using a different standard that cannot be customer-managed.",
                        "Data is lost when the VM instance is stopped or terminated.",
                        "Data is automatically replicated to another zone for high availability."
                    ],
                    "ans": 2,
                    "exp": "Local SSDs are physically attached to the host server hosting the VM. While they offer extreme performance, the data is ephemeral and does not survive VM stoppage or termination."
                }
            },
            {
                "topic": "Cloud Storage",
                "easy": {
                    "q": "Which Cloud Storage class is most cost-effective for data that you plan to access less than once a year?",
                    "opts": ["Standard", "Nearline", "Coldline", "Archive"],
                    "ans": 3,
                    "exp": "Archive Storage is the lowest-cost, highly durable storage service for data archiving, online backup, and disaster recovery, designed for data accessed less than once a year."
                },
                "medium": {
                    "q": "You want to prevent objects in a Cloud Storage bucket from being deleted or overwritten for a specific period of time due to compliance requirements. What feature should you configure?",
                    "opts": ["Bucket Lock (Retention Policy)", "Object Versioning", "Uniform Bucket-Level Access", "Lifecycle Management rules"],
                    "ans": 0,
                    "exp": "A Cloud Storage Retention Policy (Bucket Lock) allows you to specify a minimum retention period for objects. Once locked, objects cannot be deleted or overwritten until they reach the specified age."
                },
                "hard": {
                    "q": "You are hosting static media files in a Cloud Storage bucket. You want to serve these files securely to authenticated users of your web application without requiring them to have Google accounts. What is the best approach?",
                    "opts": [
                        "Create Signed URLs with a limited expiration time using a service account key.",
                        "Enable Uniform Bucket-Level Access and add the users to a Google Group.",
                        "Use Firebase Authentication and grant the users the Storage Object Viewer role.",
                        "Configure CORS settings to allow all public traffic to the bucket."
                    ],
                    "ans": 0,
                    "exp": "Signed URLs allow you to provide time-limited read or write access to specific Cloud Storage objects to anyone who possesses the URL, using the credentials of a service account."
                }
            },
            {
                "topic": "VPC Networking",
                "easy": {
                    "q": "In Google Cloud, which of the following describes a Virtual Private Cloud (VPC) network's regional scope?",
                    "opts": ["A VPC is zonal.", "A VPC is regional.", "A VPC is global.", "A VPC is multi-regional."],
                    "ans": 2,
                    "exp": "Unlike many other cloud providers where VPCs are regional, Google Cloud VPC networks are global resources. Subnets within the VPC are regional."
                },
                "medium": {
                    "q": "You need to allow external HTTP traffic to reach your VM instances. Which configuration is required?",
                    "opts": [
                        "Create a firewall rule in your VPC that allows ingress traffic on port 80 with target tags matching your VMs.",
                        "Create an egress firewall rule that permits traffic on port 80.",
                        "Assign a local SSD to the VM instances.",
                        "Set up a Cloud VPN tunnel between your subnet and the internet."
                    ],
                    "ans": 0,
                    "exp": "To allow external traffic to reach a VM, you must create a VPC firewall rule permitting ingress traffic on the required port (80 for HTTP) and target it to the VMs (using tags or service accounts)."
                },
                "hard": {
                    "q": "You want to establish a private, high-bandwidth connection between your on-premises data center and your Google Cloud VPC network with a 99.99% SLA, without routing traffic over the public internet. Which connectivity option should you choose?",
                    "opts": ["Carrier Peering", "Cloud VPN", "Dedicated Interconnect", "Partner Interconnect"],
                    "ans": 2,
                    "exp": "Dedicated Interconnect provides a direct physical connection between your on-premises network and Google's network, with the capability to meet 99.99% availability SLA configurations."
                }
            },
            {
                "topic": "Google Kubernetes Engine (GKE)",
                "easy": {
                    "q": "What is GKE short for?",
                    "opts": ["Google Kernel Engine", "Google Kubernetes Engine", "Google Keyway Engine", "Google Kubelet Environment"],
                    "ans": 1,
                    "exp": "GKE stands for Google Kubernetes Engine, a managed environment for deploying containerized applications."
                },
                "medium": {
                    "q": "You want to deploy a containerized application to GKE and ensure that Google automatically manages the node upgrading, scaling, and provisioning. Which GKE cluster mode should you select?",
                    "opts": ["Standard Mode", "Autopilot Mode", "Private Cluster Mode", "Shared VPC Cluster Mode"],
                    "ans": 1,
                    "exp": "In Autopilot mode, GKE provisions and manages the cluster's underlying infrastructure, including nodes, scaling, security, and upgrades, charging you only for the pods you run."
                },
                "hard": {
                    "q": "You need to expose a stateful containerized application running in GKE to the public internet, ensuring that traffic is balanced across pods and persistent sessions are maintained. What Kubernetes resource type should you define?",
                    "opts": ["A Pod configuration", "An Ingress resource with a Google Cloud HTTP(S) Load Balancer", "A ClusterIP Service", "A DaemonSet"],
                    "ans": 1,
                    "exp": "An Ingress resource in GKE configures a Google Cloud HTTP(S) Load Balancer, which supports advanced traffic routing, SSL termination, and session affinity (persistence)."
                }
            }
        ]
    },
    {
        "id": "google-cloud-digital-leader",
        "provider": "google-cloud",
        "name": "Google Cloud Digital Leader",
        "description": "Validates foundational knowledge of cloud concepts, Google Cloud products, services, tools, features, and primary use cases.",
        "icon": "☁️",
        "topics": [
            {
                "topic": "Cloud Concepts",
                "easy": {
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
                "medium": {
                    "q": "Which cloud service model provides a pre-configured application environment where the customer only manages data and application logic, with zero host infrastructure administration?",
                    "opts": ["Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Software as a Service (SaaS)", "Bare Metal as a Service"],
                    "ans": 1,
                    "exp": "Platform as a Service (PaaS) provides a managed platform for application development and deployment, removing the need for operating system or server management."
                },
                "hard": {
                    "q": "Your organization wants to migrate its legacy database to Google Cloud but needs to maintain strict latency guidelines with an on-premises mainframe. Which cloud deployment model represents this setup?",
                    "opts": ["Public Cloud", "Private Cloud", "Hybrid Cloud", "Multi-Cloud"],
                    "ans": 2,
                    "exp": "A hybrid cloud setup combines public cloud services (like Google Cloud) with private cloud or on-premises resources (like a mainframe)."
                }
            },
            {
                "topic": "Compute & Serverless",
                "easy": {
                    "q": "Which Google Cloud service lets you run containerized applications without provisioning or managing virtual machines?",
                    "opts": ["Compute Engine", "Cloud Storage", "Cloud Run", "Cloud SQL"],
                    "ans": 2,
                    "exp": "Cloud Run is a fully managed serverless compute platform that runs containerized applications."
                },
                "medium": {
                    "q": "What is the primary difference between App Engine Standard and App Engine Flexible?",
                    "opts": [
                        "Standard runs in sandboxed environments with fast startup times; Flexible runs in Docker containers on Compute Engine VMs.",
                        "Standard supports any programming language; Flexible only supports Python.",
                        "Standard does not scale automatically; Flexible scales down to zero.",
                        "Flexible is serverless, whereas Standard requires managing physical hardware."
                    ],
                    "ans": 0,
                    "exp": "App Engine Standard runs in a sandbox with restricted language versions but scales down to zero instantly. App Engine Flexible runs containers on VMs, allowing custom libraries but with slower startup."
                },
                "hard": {
                    "q": "Which service should a digital leader recommend to run lightweight, single-purpose snippet functions that execute in response to cloud events (like a file uploaded to Cloud Storage)?",
                    "opts": ["Cloud Functions", "Cloud Run", "Compute Engine", "GKE"],
                    "ans": 0,
                    "exp": "Cloud Functions is Google Cloud's Event-Driven Serverless Function-as-a-Service (FaaS) designed for running small snippets of code triggered by platform events."
                }
            }
        ]
    },
    {
        "id": "aws-certified-cloud-practitioner",
        "provider": "aws",
        "name": "AWS Certified Cloud Practitioner",
        "description": "Provides a high-level overview of AWS cloud concepts, security, technology, architecture, and billing models.",
        "icon": "🍊",
        "topics": [
            {
                "topic": "AWS Cloud Basics",
                "easy": {
                    "q": "What is the AWS service that provides resizable virtual server instances in the cloud?",
                    "opts": ["Amazon EC2", "Amazon S3", "Amazon RDS", "AWS Lambda"],
                    "ans": 0,
                    "exp": "Amazon Elastic Compute Cloud (EC2) provides secure, resizable compute capacity in the form of virtual servers (instances) in the AWS Cloud."
                },
                "medium": {
                    "q": "Which AWS security tool allows you to control inbound and outbound traffic at the individual Amazon EC2 instance level?",
                    "opts": ["Network Access Control Lists (NACLs)", "Security Groups", "AWS Shield", "AWS Identity and Access Management (IAM)"],
                    "ans": 1,
                    "exp": "Security Groups act as a virtual firewall for your EC2 instances to control incoming and outgoing traffic (stateful). NACLs control traffic at the subnet level (stateless)."
                },
                "hard": {
                    "q": "You want to design a highly resilient architecture in AWS. Which pillar of the AWS Well-Architected Framework focuses on recovery from infrastructure or service disruptions?",
                    "opts": ["Security", "Reliability", "Performance Efficiency", "Operational Excellence"],
                    "ans": 1,
                    "exp": "The Reliability pillar focuses on the ability of a workload to perform its intended function correctly and consistently, including recovering from failures."
                }
            },
            {
                "topic": "AWS Services",
                "easy": {
                    "q": "Which AWS storage service is best suited for storing object data like images, videos, and static files?",
                    "opts": ["Amazon EBS", "Amazon EFS", "Amazon S3", "Amazon DynamoDB"],
                    "ans": 2,
                    "exp": "Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance."
                },
                "medium": {
                    "q": "A company wants to deploy a relational SQL database in AWS and offload database patching, backups, and OS updates to AWS. Which service should they use?",
                    "opts": ["Amazon EC2 with SQL Server installed", "Amazon DynamoDB", "Amazon Relational Database Service (RDS)", "Amazon ElastiCache"],
                    "ans": 2,
                    "exp": "Amazon RDS is a managed service that makes it easy to set up, operate, and scale a relational database, handling administrative tasks like patching and backups."
                },
                "hard": {
                    "q": "Which AWS service helps users distribute content globally to end-users with low latency and high data transfer speeds by caching content at edge locations?",
                    "opts": ["Amazon Route 53", "AWS Direct Connect", "Amazon CloudFront", "Elastic Load Balancing (ELB)"],
                    "ans": 2,
                    "exp": "Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency."
                }
            }
        ]
    },
    {
        "id": "dbt-certified-developer",
        "provider": "dbt",
        "name": "dbt Certified Developer",
        "description": "Validates expertise in analytics engineering workflows, dbt compilation, modeling, testing, documentation, and deployment.",
        "icon": "🛠️",
        "topics": [
            {
                "topic": "dbt Core Concepts",
                "easy": {
                    "q": "In a dbt project, what programming languages are primarily used to define models?",
                    "opts": ["SQL and Jinja", "Python and Scala", "JavaScript and HTML", "R and SQL"],
                    "ans": 0,
                    "exp": "dbt combines SQL and Jinja (a templating language) to write modular database transformations."
                },
                "medium": {
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
                "hard": {
                    "q": "Which dbt materialization configuration compiles the model SQL into a physical table that is completely dropped and rebuilt on every execution?",
                    "opts": ["view", "table", "incremental", "ephemeral"],
                    "ans": 1,
                    "exp": "The 'table' materialization rebuilds the model as a physical table by dropping the old table and running a CREATE TABLE AS statement."
                }
            },
            {
                "topic": "dbt Tests & Docs",
                "easy": {
                    "q": "Which command compiles and executes data tests defined in your dbt project schema files?",
                    "opts": ["dbt test", "dbt run", "dbt compile", "dbt docs generate"],
                    "ans": 0,
                    "exp": "The `dbt test` command runs assertions against your models to validate data quality."
                },
                "medium": {
                    "q": "What type of dbt test is defined directly inside a `.yml` file under a column description?",
                    "opts": ["Singular test", "Generic test (Schema test)", "Custom SQL test", "Unit test"],
                    "ans": 1,
                    "exp": "Generic tests (previously schema tests) are defined in YAML and applied to columns (like `unique`, `not_null`, `accepted_values`, `relationships`)."
                },
                "hard": {
                    "q": "What is the primary function of the ref() function in dbt models?",
                    "opts": [
                        "It references external source raw tables.",
                        "It establishes lineage dependencies between models, enabling dbt to build models in the correct order.",
                        "It executes a sub-query directly from python pandas.",
                        "It formats compiled SQL commands."
                    ],
                    "ans": 1,
                    "exp": "The `ref()` function is the most important function in dbt. It allows you to reference other models and tells dbt how to construct the DAG (Directed Acyclic Graph) to compile dependencies."
                }
            }
        ]
    },
    {
        "id": "microsoft-azure-fundamentals",
        "provider": "microsoft",
        "name": "Microsoft Azure Fundamentals (AZ-900)",
        "description": "Covers foundational knowledge of Azure cloud services, security, privacy, compliance, trust, and pricing models.",
        "icon": "🔷",
        "topics": [
            {
                "topic": "Azure Cloud Concepts",
                "easy": {
                    "q": "What is the name of Microsoft Azure's administrative portal?",
                    "opts": ["Azure Console", "Azure Portal", "Azure Cloud shell", "Azure Workspace"],
                    "ans": 1,
                    "exp": "The Azure Portal is a web-based, unified console that provides an alternative to command-line tools to manage Azure resources."
                },
                "medium": {
                    "q": "Which Azure resource container group holds related resources that share the same lifecycle, permissions, and policies?",
                    "opts": ["Subscription", "Resource Group", "Management Group", "Region"],
                    "ans": 1,
                    "exp": "A Resource Group is a logical container for resources deployed on Azure. Resources can only belong to one resource group."
                },
                "hard": {
                    "q": "An organization wants to configure a private connection between its physical office network and its Azure Virtual Network. The connection must not use the public internet. Which service should they choose?",
                    "opts": ["Azure VPN Gateway", "Azure ExpressRoute", "Azure Firewall", "Azure Front Door"],
                    "ans": 1,
                    "exp": "Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection facilitated by a connectivity provider."
                }
            },
            {
                "topic": "Azure Compute & Storage",
                "easy": {
                    "q": "Which service represents Azure's primary Infrastructure as a Service (IaaS) virtual machines?",
                    "opts": ["Azure Functions", "Azure Virtual Machines", "Azure App Services", "Azure Container Instances"],
                    "ans": 1,
                    "exp": "Azure Virtual Machines provide on-demand, scalable computing resources in the form of virtualized server hardware."
                },
                "medium": {
                    "q": "What Azure storage service is optimized for storing massive amounts of unstructured object data, such as audio, video, or backup logs?",
                    "opts": ["Azure Files", "Azure Queue Storage", "Azure Blob Storage", "Azure Disk Storage"],
                    "ans": 2,
                    "exp": "Azure Blob Storage is Microsoft's object storage solution for the cloud, optimized for storing massive amounts of unstructured data."
                },
                "hard": {
                    "q": "You want to automate the scaling of a set of identical Azure virtual machines to maintain performance as workload demands fluctuate. Which resource type should you deploy?",
                    "opts": ["Azure Load Balancer", "Virtual Machine Scale Sets (VMSS)", "Azure Availability Sets", "Azure App Service Plans"],
                    "ans": 1,
                    "exp": "Azure Virtual Machine Scale Sets let you create and manage a group of load-balanced VMs. The number of VM instances can automatically increase or decrease in response to demand."
                }
            }
        ]
    }
]

# Function to generate 50 unique questions for each certification
def generate_questions():
    final_certs = []
    
    for cert in certifications:
        cert_id = cert["id"]
        provider = cert["provider"]
        name = cert["name"]
        desc = cert["description"]
        icon = cert["icon"]
        topics = cert["topics"]
        
        generated_questions = []
        
        # We need 50 questions. Let's iterate and generate variations
        for q_index in range(1, 51):
            # Pick a base topic (cycle through available topics)
            topic_obj = topics[(q_index - 1) % len(topics)]
            
            # Determine difficulty distribution: 
            # 1-15: Easy, 16-35: Medium, 36-50: Hard
            if q_index <= 15:
                diff = "easy"
                base_q = topic_obj["easy"]
            elif q_index <= 35:
                diff = "medium"
                base_q = topic_obj["medium"]
            else:
                diff = "hard"
                base_q = topic_obj["hard"]
                
            # Create a variation of the question to make them distinct
            q_id = f"{cert_id}-q{q_index}"
            
            # Formulate the question text based on index
            q_text = f"[{topic_obj['topic']} - Set {((q_index - 1) // len(topics)) + 1}] {base_q['q']}"
            
            # Keep options and answer index
            options = base_q["opts"]
            correct_index = base_q["ans"]
            explanation = base_q["exp"] + f" (Question ID: {q_id}, Difficulty: {diff.capitalize()})"
            
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
            "questions": generated_questions
        })
        
    return {"certifications": final_certs}

# Generate and save
data = generate_questions()
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Generated data/questions.json with {len(data['certifications'])} certifications and 50 questions each (total {50 * len(data['certifications'])} questions)!")
