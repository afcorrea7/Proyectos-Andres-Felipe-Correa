using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Aim : MonoBehaviour
{
    //PARA QUE PASE A TRAVES DE ELLOS, EL PREFAB DE LOS ENEMIGOS DEBE ESTAR EN LA CAPA "Ignore Raycast"

    public int numReflections; 
    public float maxRayLength; 
    public EnemyLayer enemLayer;
    [SerializeField] private LineRenderer myLineRenderer;
    private Ray ray; 
    private RaycastHit rayHit;
    
    void Start()
    {
        myLineRenderer = GetComponent<LineRenderer>(); 
    }


    public void RayoGuia(bool onOff){ //LLamado por el Script AimGun
        if(onOff){
            ray = new Ray(transform.position, transform.forward); //Ray(origin, direction)

            
            myLineRenderer.positionCount = 1; //darle dos vertices a la linea (empieza en 0)
            myLineRenderer.SetPosition(0, transform.position); //LineRenderer.SetPosition(index, position) | Que la posicion del primer vertice sea el origen, osea el arma
            float remainingRayLength = maxRayLength; //Para restarle distancia al ray después

            Debug.DrawRay(transform.position, transform.forward, Color.green);

            if(Physics.Raycast(ray.origin, ray.direction, out rayHit, remainingRayLength)){ //Checa si el primer ray creado colisiona
                if(rayHit.collider.tag == "Enemy"){ //Si es un enemigo, el primer rayo para
                    enemLayer.updateLayer(0);
                } //Este if se hace antes del for para que el primer rayo pare incluso si el segundo(que es invisible por el momento) toca un espejo,
                    //De esta forma si la guia esta apuntando a su primer reflejo pero hay un enemigo en el camino el rayo no sigue derecho
            }

            for(int i=0;i<=numReflections;i++){
                
                if(Physics.Raycast(ray.origin, ray.direction, out rayHit, remainingRayLength)){ 
                    //Physics.Raycast es un bool que se vuelve true si colisiona con algo
                    //Physics.Raycast(Vector3 origin, Vector3 direction, float maxDistance, int layerMask, queryTriggerInteraction)
                        //out hit es el output de la colision, layerMask especifica que colliders se ignoran, queryTrigger dicta si ignora trigger colliders o no

                    //Creamos un nuevo rayo desde el nuevo vertice:
                    ray = new Ray(rayHit.point-ray.direction * 0.01f, Vector3.Reflect(ray.direction, rayHit.normal)); //Vector3.Reflect(Vector3 inDirection, Vector3 inNormal)
                                                                                //inDirection toma un vector entrante, inNormal define el vector normal de un plano    

                    int newPos = myLineRenderer.positionCount += 1; //Añade un vertice a la linea
                    myLineRenderer.SetPosition(newPos-1, rayHit.point); //El origen del nuevo vertice sera donde termina el anterior               

                    remainingRayLength -= Vector3.Distance(ray.origin, rayHit.point); //Vector3.Distance(pos a, pos b) | restarle distancia desde la creacion del nuevo vertice  
                    
                    Debug.DrawRay(rayHit.point-ray.direction * 0.01f, Vector3.Reflect(ray.direction, rayHit.normal), Color.green);

                    if(rayHit.collider.tag != "Mirror"){
                        if(i==0){
                            enemLayer.updateLayer(0); //Si no hay rebotes, el rayo para
                        }else{
                            enemLayer.updateLayer(2); //Si han habido rebotes, el rayo sigue derecho
                        }
                        break; //Rompe el ciclo si pasa por algo que no es un espejo

                    }

                //else{ //Si el rayo no le esta dando a nada
                    //myLineRenderer.positionCount += 1;
                    //myLineRenderer.SetPosition(myLineRenderer.positionCount-1, ray.origin+ray.direction*remainingRayLength);
                //} 
                }
            }
        }else{
            myLineRenderer.positionCount=0;
        }
    }
}
