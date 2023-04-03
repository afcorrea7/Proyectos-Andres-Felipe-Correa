using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerGun : MonoBehaviour
{
    [SerializeField]
    Transform firingPoint;
    [SerializeField]
    float fireRate=0.1f; //firingSpeed is not the speed of the bullet, but the time interval between
    public GameObject projectilePrefab;

    [SerializeField]
    private Transform bulletParent; //Obtain a parent to store bullet clones

    public static PlayerGun Instance;
    private float lastTimeShot = 0;
    //private Transform firingPointTrans;

    void Awake()
    {
        Instance=GetComponent<PlayerGun>();
        //firingPointTrans = firingPoint.GetComponent<Transform>();
    }

    public void Shoot(){
        if (lastTimeShot + fireRate <= Time.time){ //the player can shoot every x time (shoots per second)
            lastTimeShot = Time.time;
            Instantiate(projectilePrefab,firingPoint.position, firingPoint.rotation, bulletParent.transform);  //Instantiate(object, position, rotation, parent)
        }
        
    }
}
