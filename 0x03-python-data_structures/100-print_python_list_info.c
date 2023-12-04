#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic
 *							info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int elemnt;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elemnt = 0; elemnt < Py_SIZE(p); elemnt++)
		printf("Element %d: %s\n", elemnt, Py_TYPE(PyList_GetItem(p, elemnt))->tp_name);
}

