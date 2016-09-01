#include <Python.h>

#include "tao.h"

static PyObject *tao_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    tao_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    tao_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef TaoMethods[] = {
    { "getPoWHash", tao_getpowhash, METH_VARARGS, "Returns the proof of work hash using tao hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef TaoModule = {
    PyModuleDef_HEAD_INIT,
    "tao_hash",
    "...",
    -1,
    TaoMethods
};

PyMODINIT_FUNC PyInit_tao_hash(void) {
    return PyModule_Create(&TaoModule);
}

#else

PyMODINIT_FUNC inittao_hash(void) {
    (void) Py_InitModule("tao_hash", TaoMethods);
}
#endif
