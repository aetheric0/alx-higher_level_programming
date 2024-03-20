#include <Python.h>
#include <sys/types.h>

/**
 * print_python_list_info - print info of python list
 * @p: pyObject pointer
 **/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i, allocated;
	PyObject element, element_type,
		*sys_module, *getsizeof_func, *args, size_obj;

	size = PyList_Size(p);
	sys_module = PyImport_ImportModule("sys");
	getsizeof_func = PyObject_GetAttrString(sys_module,
						"getsizeof");
	args = PyTuple_Pack(1, p);
	size_obj = PyObject_CallObject(getsizeof_func, args);
	allocated = PyLong_AsSize_t(size_obj);
	printf("[*] Size of the Python List = %d\n", size);
	printf("Allocated: %d\n", allocated);
	for (i = 0; i < size; i++)
	{
				element = PyList_GetItem(p, i);
		element_type = Py_TYPE(element);
		printf("Element %d: Type=%s\n", i, element_type->tp_name);
	}
}
