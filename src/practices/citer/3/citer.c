/**
 * FileName:   citer.c
 * Author:     Fasion Chan
 * @contact:   fasionchan@gmail.com
 * @version:   $Id$
 *
 * Description:
 *
 * Changelog:
 *
 **/

#include <Python.h>


/**
 * Iter type
 **/
typedef struct {
    // include object head
    PyObject_HEAD

    // util n, not included
	long int n;
    // current value
    long int i;
} citer_Iter;


/**
 * init function
 **/
static int citer_Iter_init(PyObject* self, PyObject* args, PyObject* kwds) {
    // pointer cast
    citer_Iter* iter = (citer_Iter*)self;

    // argument list
    // only one argument is needed: n
    static char *kw_list[] = {"n"};

    // parse args
    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|l", kw_list, &(iter->n))) {
        return -1;
    }

    // set current value to 0
    iter->i = 0;

    return 0;
}


/**
 * iter function
 **/
static PyObject* citer_Iter_iter(PyObject* self) {
    // just return itself
    Py_INCREF(self);
    return self;
}


/**
 * iternext function
 **/
static PyObject* citer_Iter_iternext(PyObject* self) {
    citer_Iter* iter = (citer_Iter*)self;

    // return current value and increase
    if (iter->i < iter->n) {
        PyObject *value = Py_BuildValue("l", iter->i);
        ++(iter->i);
        return value;
    }
    else {
        PyErr_SetNone(PyExc_StopIteration);
        return NULL;
    }
}


/**
 * Type object for Iter type
 **/
static PyTypeObject citer_IterType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "citer.Iter",            	/*tp_name*/
    sizeof(citer_Iter),       	/*tp_basicsize*/
    0,                         	/*tp_itemsize*/
    0,                         	/*tp_dealloc*/
    0,                         	/*tp_print*/
    0,                         	/*tp_getattr*/
    0,                         	/*tp_setattr*/
    0,                         	/*tp_compare*/
    0,                         	/*tp_repr*/
    0,                         	/*tp_as_number*/
    0,                         	/*tp_as_sequence*/
    0,                         	/*tp_as_mapping*/
    0,                         	/*tp_hash */
    0,                        	/*tp_call*/
    0,                        	/*tp_str*/
    0,                        	/*tp_getattro*/
    0,                        	/*tp_setattro*/
    0,                        	/*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "Iter object.",           	/* tp_doc */
    0, 							/* tp_traverse */
    0, 							/* tp_clear */
    0, 							/* tp_richcompare */
    0, 							/* tp_weaklistoffset */
    citer_Iter_iter,  			/* tp_iter: __iter__() method */
    citer_Iter_iternext,  		/* tp_iternext: next() method */
	0,             				/* tp_methods */
    0,             				/* tp_members */
    0,                        	/* tp_getset */
    0,                        	/* tp_base */
    0,                        	/* tp_dict */
    0,                        	/* tp_descr_get */
    0,                        	/* tp_descr_set */
    0,                        	/* tp_dictoffset */
    (initproc)citer_Iter_init,	/* tp_init */
    0,                        	/* tp_alloc */
    PyType_GenericNew,          /* tp_new */
};

/**
 * module defination
 **/
static PyModuleDef citer_module = {
    PyModuleDef_HEAD_INIT,
    "citer",
    "Iter type for c iterator tutorial.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};


/**
 * module init function, called when being imported
 **/
PyMODINIT_FUNC
PyInit_citer(void) {
    // initialize new data type
    if (PyType_Ready(&citer_IterType) < 0) {
        return NULL;
    }

    // create module object
	PyObject* module = PyModule_Create(&citer_module);
    if (NULL == module) {
        return NULL;
    }

    // add new type to module
    Py_INCREF(&citer_IterType);
    PyModule_AddObject(module, "Iter", (PyObject*)&citer_IterType);

    return module;
}
