using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IgnoreOtherColliders : MonoBehaviour
{
    int enemyPunchLayer;
    int playerPunchLayer;
    // Start is called before the first frame update
    void Start()
    {
        enemyPunchLayer = LayerMask.NameToLayer("EnemyPunchLayer");
        playerPunchLayer = LayerMask.NameToLayer("PunchLayer");
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        Physics2D.IgnoreLayerCollision(enemyPunchLayer, playerPunchLayer);
    }
}
