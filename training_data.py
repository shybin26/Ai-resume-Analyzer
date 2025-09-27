# In training_data.py

TRAIN_DATA = [
    # Web Development
    ("Developed web applications using React and Node.js.", {"entities": [(30, 35, "LIBRARY"), (40, 47, "LIBRARY")]}),
    ("Built scalable REST APIs with Python and the Django framework.", {"entities": [(18, 26, "SKILL"), (32, 38, "SKILL"), (47, 53, "LIBRARY")]}),
    ("Experienced in frontend development with Vue.js and TypeScript.", {"entities": [(35, 41, "LIBRARY"), (46, 56, "SKILL")]}),
    ("Maintained a legacy codebase written in PHP and jQuery.", {"entities": [(37, 40, "SKILL"), (45, 51, "LIBRARY")]}),
    ("Designed and implemented microservices using Java and Spring Boot.", {"entities": [(28, 40, "SKILL"), (47, 51, "SKILL"), (56, 67, "LIBRARY")]}),
    ("Proficient in modern JavaScript (ES6+) and CSS Flexbox.", {"entities": [(17, 27, "SKILL"), (35, 46, "SKILL")]}),
    ("Worked with GraphQL to optimize data fetching for our applications.", {"entities": [(12, 20, "SKILL")]}),
    ("Experience building user interfaces with Angular and RxJS.", {"entities": [(38, 45, "LIBRARY"), (50, 54, "LIBRARY")]}),
    ("Developed backend services using the Flask microframework.", {"entities": [(34, 39, "LIBRARY")]}),
    ("Integrated third-party APIs such as Stripe and Twilio.", {"entities": [(35, 41, "SOFTWARE"), (46, 52, "SOFTWARE")]}),

    # Cloud & DevOps
    ("Managed cloud infrastructure on AWS, utilizing EC2 and S3.", {"entities": [(30, 33, "CLOUD"), (45, 48, "SKILL"), (53, 55, "SKILL")]}),
    ("Automated deployment pipelines using Jenkins and Docker.", {"entities": [(34, 41, "SOFTWARE"), (46, 52, "SOFTWARE")]}),
    ("Worked extensively with Microsoft Azure for cloud solutions.", {"entities": [(25, 41, "CLOUD")]}),
    ("Knowledge of container orchestration with Kubernetes.", {"entities": [(38, 48, "SOFTWARE")]}),
    ("Implemented Infrastructure as Code (IaC) with Terraform.", {"entities": [(42, 45, "SKILL"), (51, 60, "SOFTWARE")]}),
    ("Monitored system performance using Prometheus and Grafana.", {"entities": [(34, 44, "SOFTWARE"), (49, 56, "SOFTWARE")]}),
    ("Certified in Google Cloud Platform (GCP) as an Associate Cloud Engineer.", {"entities": [(13, 36, "CERTIFICATION")]}),
    ("Familiar with CI/CD practices and tools like GitLab.", {"entities": [(14, 19, "METHODOLOGY"), (40, 46, "SOFTWARE")]}),
    ("Wrote Ansible playbooks for configuration management.", {"entities": [(6, 13, "SOFTWARE")]}),
    ("Deployed serverless functions on AWS Lambda.", {"entities": [(32, 43, "SKILL")]}),

    # Data Science & ML
    ("Performed data analysis and visualization with R and Tableau.", {"entities": [(44, 45, "SKILL"), (50, 57, "SOFTWARE")]}),
    ("Skilled in machine learning with Scikit-learn and TensorFlow.", {"entities": [(32, 44, "LIBRARY"), (49, 59, "LIBRARY")]}),
    ("Built NLP models using PyTorch and the transformers library.", {"entities": [(24, 31, "LIBRARY"), (40, 52, "LIBRARY")]}),
    ("Cleaned and preprocessed large datasets using Pandas and NumPy.", {"entities": [(46, 52, "LIBRARY"), (57, 62, "LIBRARY")]}),
    ("Engineered features for predictive models in the financial sector.", {"entities": []}), # Example of a sentence with no labeled entities
    ("Experience with big data technologies like Apache Spark and Hadoop.", {"entities": [(41, 54, "SOFTWARE"), (59, 66, "SOFTWARE")]}),
    ("Developed deep learning solutions with Keras.", {"entities": [(36, 41, "LIBRARY")]}),
    ("Queried data from warehouses using complex SQL statements.", {"entities": [(40, 43, "SKILL")]}),
    ("Used Jupyter Notebooks for exploratory data analysis.", {"entities": [(5, 22, "SOFTWARE")]}),
    ("Created interactive dashboards with Plotly and Dash.", {"entities": [(34, 40, "LIBRARY"), (45, 49, "LIBRARY")]}),

    # Project Management & Design
    ("Certified Scrum Master with experience in Agile frameworks.", {"entities": [(10, 22, "CERTIFICATION"), (42, 47, "METHODOLOGY")]}),
    ("Designed user interfaces and prototypes with Figma and Sketch.", {"entities": [(43, 48, "SOFTWARE"), (53, 59, "SOFTWARE")]}),
    ("Holder of the PMP certification for project management.", {"entities": [(15, 18, "CERTIFICATION")]}),
    ("Tracked project tasks and sprints using Jira and Confluence.", {"entities": [(39, 43, "SOFTWARE"), (48, 58, "SOFTWARE")]}),
    ("Created wireframes and user flows with Adobe XD.", {"entities": [(38, 46, "SOFTWARE")]}),
    ("Led daily stand-ups following the Scrum methodology.", {"entities": [(34, 39, "METHODOLOGY")]}),
    ("Managed stakeholder expectations and project timelines.", {"entities": []}),
    ("Familiar with Kanban for workflow management.", {"entities": [(14, 20, "METHODOLOGY")]}),
    ("Used Trello for lightweight task tracking.", {"entities": [(5, 11, "SOFTWARE")]}),
    ("A/B testing of user interfaces to improve conversion rates.", {"entities": [(0, 11, "SKILL")]}),

    # General & Other
    ("Experience in version control systems like Git and SVN.", {"entities": [(40, 43, "TOOL"), (48, 51, "TOOL")]}),
    ("Built mobile applications for iOS using Swift.", {"entities": [(30, 33, "PLATFORM"), (40, 45, "SKILL")]}),
    ("Expertise in object-oriented programming with C# and .NET.", {"entities": [(43, 45, "SKILL"), (50, 54, "LIBRARY")]}),
    ("Utilized Salesforce for customer relationship management.", {"entities": [(10, 20, "SOFTWARE")]}),
    ("Developed native Android apps with Kotlin.", {"entities": [(18, 25, "PLATFORM"), (34, 40, "SKILL")]}),
    ("Wrote technical documentation for APIs using Swagger.", {"entities": [(43, 50, "TOOL")]}),
    ("Tested APIs with Postman and automated scripts.", {"entities": [(18, 25, "SOFTWARE")]}),
    ("My primary development environment is VS Code.", {"entities": [(37, 44, "SOFTWARE")]}),
    ("Administered Linux servers running Ubuntu.", {"entities": [(14, 19, "PLATFORM"), (31, 37, "PLATFORM")]}),
    ("Completed the CompTIA Network+ certification.", {"entities": [(14, 32, "CERTIFICATION")]})
]