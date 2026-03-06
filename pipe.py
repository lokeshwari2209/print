#EXP 1
#VERSION 1:
#PIPELINE SCRIPT:
pipeline {
    agent any

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello Jenkins', description: 'Message to display')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/sample-repo/demo.git'
            }
        }

        stage('Print Parameter') {
            steps {
                echo "Message entered: ${params.MESSAGE}"
            }
        }

        stage('Run Batch Command') {
            steps {
                bat 'echo Hello from Jenkins'
            }
        }

    }
}
VERSION 2:
pipeline {
    agent any

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello Jenkins', description: 'Message to display')
    }

    stages {

        stage('Checkout Updated Code') {
            steps {
                git 'https://github.com/USERNAME/REPOSITORY.git'
            }
        }

        stage('Display System Date') {
            steps {
                bat 'date /t'
            }
        }

        stage('Print Parameter Again') {
            steps {
                echo "Parameter value is: ${params.MESSAGE}"
            }
        }

    }
}
VERSION 3:
pipeline {
    agent any

    stages {

        stage('Checkout Latest Code') {
            steps {
                git 'https://github.com/USERNAME/REPOSITORY.git'
            }
        }

        stage('Create File') {
            steps {
                bat 'echo This file is created by Jenkins > output.txt'
            }
        }

        stage('Display File Content') {
            steps {
                bat 'type output.txt'
            }
        }

    }
}
VERSION 4:
pipeline {
    agent any

    parameters {
        string(name: 'USERNAME', defaultValue: 'student', description: 'Enter username')
    }

    stages {

        stage('Checkout Latest Code') {
            steps {
                git 'https://github.com/USERNAME/REPOSITORY.git'
            }
        }

        stage('Create User File') {
            steps {
                bat 'echo %USERNAME% > user.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type user.txt'
            }
        }

    }
}






Experiment 2
Version 1:
pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_TEST', defaultValue: false, description: 'Run the test stage')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Run Test') {
            when {
                expression { params.RUN_TEST == true }
            }
            steps {
                bat 'echo Running Test'
            }
        }

    }
}
VERSION 2:
pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['DEV', 'TEST', 'PROD'],
            description: 'Select the environment'
        )
    }

    stages {

        stage('Checkout Updated Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Print Selected Environment') {
            steps {
                bat "echo Selected Environment: ${params.ENVIRONMENT}"
            }
        }

    }
}
VERSION 3:
pipeline {
    agent any

    parameters {
        string(name: 'BUILD_NAME', defaultValue: '', description: 'Enter build name')
    }

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Create File') {
            steps {
                bat "echo ${params.BUILD_NAME} > build.txt"
            }
        }

    }
}
VERSION 4:
pipeline {
    agent any

    parameters {
        string(name: 'NAME', defaultValue: 'User', description: 'Enter name')
        booleanParam(name: 'RUN_TEST', defaultValue: false, description: 'Run test stage')
        choice(name: 'ENV', choices: ['DEV', 'TEST', 'PROD'], description: 'Select environment')
    }

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Display Workspace Path') {
            steps {
                bat 'echo Workspace Path: %WORKSPACE%'
            }
        }

        stage('Print Parameter Values') {
            steps {
                bat "echo NAME: ${params.NAME}"
                bat "echo RUN_TEST: ${params.RUN_TEST}"
                bat "echo ENV: ${params.ENV}"
            }
        }

    }
}
EXPERIMENT 3:
VERSION 1:
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Compile') {
            steps {
                bat 'echo Compiling...'
            }
        }

        stage('Build Success') {
            steps {
                bat 'echo Build Successful!'
            }
        }

    }
}
VERSION 2:
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Create Build Folder') {
            steps {
                bat 'mkdir build'
            }
        }

        stage('Copy Files to Build Folder') {
            steps {
                bat 'copy * build'
            }
        }

    }
}
VERSION 3:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('List Files in Workspace') {
            steps {
                bat 'dir'
            }
        }

        stage('Print Build Timestamp') {
            steps {
                bat 'echo Build Time: %DATE% %TIME%'
            }
        }

    }
}
VERSION 4:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Create Artifact File') {
            steps {
                bat 'echo This is a build artifact > artifact.txt'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'artifact.txt'
            }
        }

    }
}
EXPERIMENT 4:
VERSION 1:
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                // Task 1: Checkout code from GitHub
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Approval Step') {
            steps {
                // Task 2: Ask user confirmation
                input message: 'Proceed with Build?'
            }
        }

        stage('Confirmation') {
            steps {
                // Task 3: Print message after approval
                echo 'Build approved! Continuing the pipeline...'
            }
        }
    }
}
VERSION 2:
pipeline {
    agent any

    parameters {
        string(name: 'APPROVAL', defaultValue: 'YES', description: 'Enter approval to continue')
    }

    stages {

        stage('Checkout Repository') {
            steps {
                // Task 1: Checkout updated repository
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('User Input') {
            steps {
                // Task 2: Display user input parameter
                echo "User approval input: ${params.APPROVAL}"
            }
        }

        stage('BAT Command') {
            steps {
                // Task 3: Execute BAT command to display confirmation
                bat 'echo Build Approved! Continuing execution...'
            }
        }

    }
}
VERSION 3:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                // Task 1: Checkout repository
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Print Build Number') {
            steps {
                // Task 2: Print Jenkins build number
                echo "Jenkins Build Number: ${env.BUILD_NUMBER}"
            }
        }

        stage('Display Status') {
            steps {
                // Task 3: Display status message
                echo "Pipeline executed successfully."
            }
        }

    }
}
VERSION 4:
pipeline {
    agent any

    parameters {
        string(name: 'TEXT_VALUE', defaultValue: 'Hello', description: 'Enter text')
    }

    stages {

        stage('Checkout Repository') {
            steps {
                // Task 1: Checkout repository
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Display Parameter') {
            steps {
                // Task 2: Accept and display text parameter
                echo "User entered: ${params.TEXT_VALUE}"
            }
        }

        stage('Save to File') {
            steps {
                // Task 3: Save parameter value into file using BAT
                bat "echo ${params.TEXT_VALUE} > output.txt"
            }
        }

    }
}
EXPERIMENT 5:
VERSION1:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Create sample.txt') {
            steps {
                bat 'echo This is a sample file created by Jenkins > sample.txt'
            }
        }

        stage('Display File Content') {
            steps {
                bat 'type sample.txt'
            }
        }

    }
}


VERSION 2:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Append Data to File') {
            steps {
                bat 'echo Adding new line to sample file >> sample.txt'
            }
        }

        stage('Count Lines in File') {
            steps {
                bat 'find /c /v "" sample.txt'
            }
        }

    }
}
VERSION 3:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Rename File') {
            steps {
                bat 'rename sample.txt newfile.txt'
            }
        }

        stage('List Files') {
            steps {
                bat 'dir'
            }
        }

    }
}
VERSION 4:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Delete File') {
            steps {
                bat 'del sample.txt'
            }
        }

        stage('Confirm Deletion') {
            steps {
                bat 'dir'
            }
        }

    }
}
EXPERIMENT 6:
VERSION 1:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Print Environment Variables') {
            steps {
                bat 'set'
            }
        }

        stage('Custom Echo Message') {
            steps {
                echo "Hello! This is a custom message from Jenkins Pipeline."
            }
        }

    }
}
VERSION 2:
pipeline {
    agent any

    environment {
        MY_VAR = "Hello_Jenkins"
    }

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Print Environment Variable') {
            steps {
                bat 'echo %MY_VAR%'
            }
        }

    }
}
VERSION 3:
pipeline {
    agent any

    parameters {
        string(name: 'VERSION', defaultValue: '1.0', description: 'Enter application version')
    }

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Create Version File') {
            steps {
                bat 'echo %VERSION% > version.txt'
            }
        }

    }
}
#VERSION 4:
pipeline {
    agent any

    stages {

        stage('Checkout Repository') {
            steps {
                git 'https://github.com/your-repository-url.git'
            }
        }

        stage('Print Commit ID') {
            steps {
                bat 'git rev-parse HEAD'
            }
        }

        stage('Display Build Result') {
            steps {
                echo "Build completed successfully!"
            }
        }

    }
}


git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

git init
git clone <repository_url>

git status
git add <file_name>
git add .
git commit -m "commit message"

git log
git log --oneline

git branch
git branch <branch_name>
git checkout <branch_name>
git checkout -b <branch_name>

git merge <branch_name>

git remote add origin <repository_url>
git remote -v

git push origin <branch_name>
git push -u origin main

git pull origin main
git fetch

git diff
git reset <file_name>
git reset --hard

git rm <file_name>
git mv <old_name> <new_name>

git stash
git stash pop

git tag <tag_name>

git show
git help



git clone <repo_url>
git status
git add .
git commit -m "message"
git push origin main


#to modify
git status
git add .
git commit -m "initialmodified"
git push origin main



## if any error shows after pushing 
git pull origin main
git commit -m "merge"
git push -u origin main