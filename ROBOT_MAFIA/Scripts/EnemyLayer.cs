using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyLayer : MonoBehaviour
{
    //Layers are int numbers but can be named, in this case is easier to send a number from other Scripts so we are sticking to numbers

    //To have in mind, Layers are as follows:
    //0: Default
    //1: Transparent FX
    //2: Ignore Raycast
    //4: Water
    //5: UI

    void Start()
    {
        int LayerIgnoreRaycast = LayerMask.NameToLayer("Ignore Raycast");
    }

    //This script should be attached to the parent object where all the enemies are kept, If you try to attach it to the prefab itself changes will only be made to the
    //prefab in-folder and not the enemies currently in the scene.
    public void updateLayer(int layerNum){
        foreach (Transform child in transform)
         {
                 child.gameObject.layer = layerNum; //That's why we use child.gameObject instead of the enemy object
         }
        Debug.Log("Current layer: " + gameObject.layer);
    }

    public void toggleTrigger(bool toggle){
        foreach (Transform child in transform){
            var collidersObj = gameObject.GetComponentsInChildren<Collider>();

            for (var index = 0; index < collidersObj.Length; index++)
            {
                var colliderItem = collidersObj[index];
                colliderItem.isTrigger= toggle;
            }
        }
    }
}
