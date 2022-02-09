import subprocess
import os
bashcommand="find /spack/opt/ -name Nekbone"
process = subprocess.Popen(bashcommand.split(),stdout=subprocess.PIPE)
output,error=process.communicate()
nekbone_install_path = output.decode("utf-8").strip()
test_example_path = nekbone_install_path+"/test/example1"
filename = test_example_path + "/makenek"
src_dir = nekbone_install_path+"/src"

bashcommand ="find /spack/opt/ -name mpicc" 
process = subprocess.Popen(bashcommand.split(),stdout=subprocess.PIPE)
output,error=process.communicate()
mpicc_bin_path = output.decode("utf-8").strip()
mpicc_list = mpicc_bin_path.split("/")
nmpicc = '\/'.join(mpicc_list)
sedcommand = "sed -i -e \'s/mpicc/"+nmpicc+"/g\' "
bashcommand = sedcommand + filename
subprocess.call(bashcommand,shell=True)

bashcommand ="find /spack/opt/ -name mpif77" 
process = subprocess.Popen(bashcommand.split(),stdout=subprocess.PIPE)
output,error=process.communicate()
mpif77_bin_path = output.decode("utf-8").strip()
mpif77_list = mpif77_bin_path.split("/")
nmpif77 = '\/'.join(mpif77_list)
sedcommand = "sed -i -e \'s/mpif77/"+nmpif77+"/g\' "
bashcommand = sedcommand + filename
subprocess.call(bashcommand,shell=True)

cur_path = os.getcwd()
os.chdir(test_example_path)
bashcommand = "./makenek -d "+src_dir
subprocess.call(bashcommand,shell=True)
