echo ""
echo "Comenzaremos con la actualización"
cd /home/clau/Desktop/GestionActivos/gestion_activos
echo ""
git checkout master
echo ""
echo "Conectamos al repositorio para actualizar"
git pull
echo ""
echo ""
echo "Reiniciamos los servicios"
service start uwsgi
echo ""
echo ""
service restart nginx
echo ""
echo ""
read -p "Precione una tecla para finalizar... " -n1 -s