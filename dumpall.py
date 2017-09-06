import subprocess
from os import listdir

def dumpall():
	for f in listdir("/devops/containers"):
		if(f[0]!="."):
			with open('/devops/backup/database_dumps/'+f+'_database.dump','w') as outfile:
				subprocess.call(('docker exec -it '+f+'_database pg_dumpall -U postgres').split(),stdout=outfile)

if __name__ == "__main__":
	dumpall()
