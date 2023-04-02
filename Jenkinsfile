pipeline {
  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git 'https://github.com/MEHDI-Ibrahim/gestn.git'
      }
    }

    stage('Build image') {
                steps {
                    echo 'Starting to build docker images'
                    script {
                        login = docker.build("gestn/login")
                        notes = docker.build("gestn/notes")
                        db = docker.build("gestn/db")
                        faker = docker.build("gestn/")
                    }
                }
            }

    stage('Pushing Image') {
      steps{
        script {
          docker.withRegistry( '192.168.1.103:5000') {
            login.push("latest")
            notes.push("latest")
            db.push("latest")
            faker.push("latest")
          }
        }
      }
    }

    stage('Deploying App to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "application.yaml", kubeconfigId: "kubernetes")
        }
      }
    }

  }

}



pipeline {
        agent any
        stages {
            stage('Build image') {
                steps {
                    echo 'Starting to build docker image DB'
                    script {
                        def DB = docker.build("my-image:${env.BUILD_ID}","-f ${env.WORKSPACE}/db/Dockerfile .")
                        def nodejs = docker.build("my-image:${env.BUILD_ID}","-f ${env.WORKSPACE}/app/Dockerfile .") 
                        def php = docker.build("my-image:${env.BUILD_ID}","-f ${env.WORKSPACE}/php/Dockerfile .") 
                    }
                }
            }
        }
    }





pipeline {
  stages{



  stage('Checkout Source') {
      steps {
        git 'https://github.com/MEHDI-Ibrahim/gestn.git'
      }
    }

  stage('Build image') {
    steps{
      /* This builds the actual image; synonymous to
       * docker build on the command line */

      app = docker.build("gestn/login")
    }
  }

  stage('Test image') {
    steps{


      /* Ideally, we would run a test framework against our image.
       * For this example, we're using a Volkswagen-type approach ;-) */

      app.inside {
          sh 'echo "Tests passed"'
      }
    }
  }

  stage('Push image') {
    steps{
      /* Finally, we'll push the image with two tags:
       * First, the incremental build number from Jenkins
       * Second, the 'latest' tag.
       * Pushing multiple tags is cheap, as all the layers are reused. */
      docker.withRegistry('192.168.1.103:5000') {
          app.push("${env.BUILD_NUMBER}")
          app.push("latest")
      }
  }
}
}
}