#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int iam;
	PyListObject *objet = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", objet->allocated);
	for (iam = 0; iam < size; iam++)
		printf("Element %i: %s\n", iam, Py_TYPE(objet->ob_item[iam])->tp_name);
}
