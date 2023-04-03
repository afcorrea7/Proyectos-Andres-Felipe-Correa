using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestructableRigidbody2D : MonoBehaviour
{
    public Vector2 forceDirection;
    public float torque;

    Rigidbody2D rb;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        rb.AddForce(forceDirection);
        rb.AddTorque(torque);
    }
}
