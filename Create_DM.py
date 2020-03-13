import sys
import os

def create_dm():
  try:
      deployment_name = raw_input('Enter Deployment Name: ')
      template_fileName = raw_input('Enter Template File Name: ')
      template_filePath = os.getcwd() + '/Tmpl/' + template_fileName + '.tmpl'
      config_fileName = template_fileName + '.yaml'
      os.system('envsubst < {0} > {1}'.format(template_filePath, config_fileName))
      choice = raw_input('1. Create New Deployment Manager\n2. Update Deployment Manager\nEnter your choice: ')
      if choice == '1':
          deployment_manager_cmd = 'gcloud deployment-manager deployments \
                                    create {0} --config {1} --automatic-rollback-on-error'.format(
                                    deployment_name, config_fileName)
      elif choice == '2':
          deployment_manager_cmd = 'gcloud deployment-manager deployments \
                                update {0} --config {1} '.format(
                                deployment_name, config_fileName)
      else:
          print('Invalid Choice!')
      os.system(deployment_manager_cmd)
  except Exception as e:
      print(str(e))
      print("Exception in creating deployment manager")


def enable_gcloud_apis():
    try:
        gcloud_service_list = {'deploymentmanager.googleapis.com',
                                'sqladmin.googleapis.com',
                                'storage-api.googleapis.com',
                              }
    # - network: https://www.googleapis.com/compute/v1/projects/yogendra-humango-practice/global/networks/default
        for each in gcloud_service_list:
            cmd = 'gcloud services enable {0}'.format(each)
            print(cmd)
            os.system(cmd)
    except Exception as e:
        print("Exception in enabling service")
    return True

api_enable_choice = raw_input("Do you want to enable Api's: ")
if api_enable_choice.lower() == 'yes' or api_enable_choice.lower() == 'y':
    enable_gcloud_apis()
create_dm()