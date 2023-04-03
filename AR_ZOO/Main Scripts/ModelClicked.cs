using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ModelClicked : MonoBehaviour
{
    public GameObject panelInfo;

    void Start()
    {
        panelInfo.SetActive(false);
    }

    void Update()
    {
        
    }

    void OnMouseDown()
    {
        Debug.Log("Mouse click on "+this.gameObject);
        panelInfo.SetActive(true);
    }
}
