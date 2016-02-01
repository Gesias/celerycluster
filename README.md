# celerycluster
Origin http://octopress.pztrick.com/blog/2013/05/11/my-first-fabric-plus-celery-cluster-project/


## To run
Activate virtual env and then start the workque
celery worker -n pi -Q pi-standard --loglevel=INFO -A celeryconfig --concurrency=1

Then start scheduling the jobs
python client
