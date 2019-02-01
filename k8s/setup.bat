rem you need to run this shellscript as an administrator

rem install kubectl
rem https://kubernetes.io/docs/setup/release/notes/
for /f %%i in ('curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt') do set kctlver=%%i
if "%kctlver%" == "" exit /B 1
curl -LO https://storage.googleapis.com/kubernetes-release/release/%kctlver%/bin/windows/amd64/kubectl.exe
move kubectl.exe %systemroot%\system32

rem install minikube
rem https://github.com/kubernetes/minikube/releases
set k8ver=v0.33.1
curl -LO https://storage.googleapis.com/minikube/releases/%k8ver%/minikube-windows-amd64.exe
ren minikube-windows-amd64.exe minikube.exe
move minikube.exe %systemroot%\system32

minikube version
minikube start
minikube status

rem install helm
rem https://github.com/helm/helm/releases
set helmver=v2.12.3
curl -LO https://storage.googleapis.com/kubernetes-helm/helm-%helmver%-windows-amd64.zip
powershell -command "Expand-Archive .\helm-%helmver%-windows-amd64.zip .\helm"
move .\helm\windows-amd64\helm.exe %systemroot%\system32
del helm-%helmver%-windows-amd64.zip
rmdir /s /Q .\helm
helm init

rem wait till everything is up and running
timeout 120

rem show the dashboard
start /b minikube dashboard

exit /B 0
