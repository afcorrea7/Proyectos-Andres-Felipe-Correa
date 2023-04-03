using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    [SerializeField] private LayerMask targetLayer;
    [SerializeField] private float rotationRate = 3.0f;
    [SerializeField] private bool xRotation;
    [SerializeField] private bool yRotation;
    [SerializeField] private bool invertX;
    [SerializeField] private bool invertY;
    private float m_previousX;
    private float m_previousY;
    private bool m_rotating = false;
    private void Update()
    {

        if (Input.GetMouseButtonDown(0))
        {
            m_rotating = true;
            m_previousX = Input.mousePosition.x;
            m_previousY = Input.mousePosition.y;
        }
        
        if (Input.GetMouseButton(0))
        {
            var touch = Input.mousePosition;
            var deltaX = -(Input.mousePosition.y - m_previousY) * rotationRate;
            var deltaY = -(Input.mousePosition.x - m_previousX) * rotationRate;
            if (!yRotation) deltaX = 0;
            if (!xRotation) deltaY = 0;
            if (invertX) deltaY *= -1;
            if (invertY) deltaX *= -1;
            transform.Rotate(deltaX, deltaY, 0, Space.World);

            m_previousX = Input.mousePosition.x;
            m_previousY = Input.mousePosition.y;
        }
        if (Input.GetMouseButtonUp(0))
            m_rotating = false;
    }
}
