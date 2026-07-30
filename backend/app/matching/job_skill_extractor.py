import re


SKILL_DATABASE = [

    # =========================
    # Programming Languages
    # =========================
    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",
    "php",
    "go",
    "golang",
    "rust",
    "kotlin",
    "swift",
    "dart",
    "scala",
    "r",

    # =========================
    # Frontend
    # =========================
    "html",
    "css",
    "sass",
    "scss",
    "bootstrap",
    "tailwind",
    "react",
    "next.js",
    "angular",
    "vue",
    "nuxt",
    "jquery",
    "redux",
    "frontend",
    "responsive design",

    # =========================
    # Backend
    # =========================
    "node.js",
    "express",
    "nestjs",
    "fastapi",
    "django",
    "flask",
    "spring",
    "spring boot",
    "spring mvc",
    "spring security",
    "hibernate",
    "jpa",
    "laravel",
    "asp.net",
    ".net",
    "backend",
    "microservices",
    "rest api",
    "restful",
    "graphql",
    "soap",

    # =========================
    # Database
    # =========================
    "sql",
    "postgresql",
    "mysql",
    "mariadb",
    "oracle",
    "sql server",
    "mongodb",
    "redis",
    "sqlite",
    "elasticsearch",
    "firebase",
    "dynamodb",

    # =========================
    # Cloud
    # =========================
    "aws",
    "azure",
    "gcp",
    "ec2",
    "s3",
    "lambda",
    "cloudformation",

    # =========================
    # DevOps
    # =========================
    "docker",
    "kubernetes",
    "jenkins",
    "github actions",
    "gitlab ci",
    "terraform",
    "ansible",
    "openshift",
    "nginx",
    "apache",

    # =========================
    # Version Control
    # =========================
    "git",
    "github",
    "gitlab",
    "bitbucket",

    # =========================
    # Messaging
    # =========================
    "rabbitmq",
    "kafka",
    "activemq",

    # =========================
    # Testing
    # =========================
    "junit",
    "mockito",
    "selenium",
    "cypress",
    "pytest",
    "jest",

    # =========================
    # AI / Data
    # =========================
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "computer vision",
    "opencv",
    "tensorflow",
    "keras",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",

    # =========================
    # RPA
    # =========================
    "uipath",
    "automation anywhere",
    "blue prism",
    "power automate",
    "rpa",

    # =========================
    # SAP
    # =========================
    "sap",
    "sap hana",
    "abap",

    # =========================
    # Mobile
    # =========================
    "android",
    "ios",
    "flutter",
    "react native",

    # =========================
    # Tools
    # =========================
    "jira",
    "confluence",
    "postman",
    "swagger",
    "openapi",
    "maven",
    "gradle",
    "linux",
    "ubuntu",
    "bash",
    "terminal",

    # =========================
    # Security
    # =========================
    "oauth",
    "jwt",
    "oauth2",

    # =========================
    # Architecture
    # =========================
    "clean architecture",
    "design patterns",
    "oop",
    "object oriented programming",
    "mvc",
    "ci/cd"
]


def extract_job_skills(text: str):

    if not text:
        return []


    text = text.lower()


    found_skills = []


    for skill in SKILL_DATABASE:

        # kelime sınırı ile ara
        pattern = r"\b" + re.escape(skill) + r"\b"


        if re.search(pattern, text):

            found_skills.append(skill)


    return list(
        dict.fromkeys(found_skills)
    )