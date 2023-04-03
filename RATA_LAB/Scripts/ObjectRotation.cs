/*
    Rata Lab - Andrés Felipe Correa
    2023
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectRotation : MonoBehaviour
{
    public Vector3 _v;
    public float _rotSpeed=50.0f;

    void Update()
    {
        transform.Rotate(_v * _rotSpeed * Time.deltaTime);
    }
}
