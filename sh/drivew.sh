echo "$1 from your Google Drive"

arr=(Downloads Documents Softwares Videos Pictures)

for folder in ${arr[*]}
do
	drive $1 --no-prompt $folder
done
