/*
    Robot Mafia - Andrés Felipe Correa
    2023
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyHealth : MonoBehaviour
{
    public float enemyHealth=1f;
    public BoxCollider thisColl;
    public Bullet bullet;
    public GameObject deathParticles;
    //public GameObject enemyDeathFab; //For playing the death animation
    private BoxCollider bulletColl;

    void Update()
    {
        if(enemyHealth<=0){
            //Instantiate(enemyDeathFab, transform.position, transform.rotation); //Instantiate(object, position, rotation, parent)
            Instantiate(deathParticles, this.gameObject.transform);
            Destroy(this.gameObject,0.2f);
        }
    }

    private void OnCollisionEnter(Collision other){
        if(other.collider.tag=="Bullet"){
            enemyHealth -= 0.1f;
        }
    }
    private void OnTriggerEnter(Collider other) {
        if(other.GetComponent<Collider>().tag=="Bullet"){
            enemyHealth -= 1f;
        }
        
    }
}
