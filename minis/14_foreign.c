#include <Python.h>

void matrix_multiply(double **A, double **B, double **C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void matrix_power(double **A, double **C, int n, int power) {
    double **temp = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        temp[i] = (double *)malloc(n * sizeof(double));
        for (int j = 0; j < n; j++) {
            temp[i][j] = A[i][j];
        }
    }

    for (int p = 1; p < power; p++) {
        matrix_multiply(temp, A, C, n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp[i][j] = C[i][j];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        free(temp[i]);
    }
    free(temp);
}

static PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    PyObject *input_list;
    int power;

    if (!PyArg_ParseTuple(args, "Oi", &input_list, &power)) {
        return NULL;
    }

    if (!PyList_Check(input_list)) {
        PyErr_SetString(PyExc_TypeError, "args_err");
        return NULL;
    }

    Py_ssize_t rows = PyList_Size(input_list);
    Py_ssize_t cols = PyList_Size(PyList_GetItem(input_list, 0));

    double **A = (double **)malloc(rows * sizeof(double *));
    double **C = (double **)malloc(rows * sizeof(double *));
    for (Py_ssize_t i = 0; i < rows; i++) {
        A[i] = (double *)malloc(cols * sizeof(double));
        C[i] = (double *)malloc(cols * sizeof(double));
        for (Py_ssize_t j = 0; j < cols; j++) {
            PyObject *value = PyList_GetItem(PyList_GetItem(input_list, i), j);
            A[i][j] = PyFloat_AsDouble(value);
        }
    }

    matrix_power(A, C, rows, power);

    PyObject *result = PyList_New(rows);
    for (Py_ssize_t i = 0; i < rows; i++) {
        PyObject *row = PyList_New(cols);
        for (Py_ssize_t j = 0; j < cols; j++) {
            PyObject *new_value = PyFloat_FromDouble(C[i][j]);
            PyList_SetItem(row, j, new_value);
        }
        PyList_SetItem(result, i, row);
    }

    for (Py_ssize_t i = 0; i < rows; i++) {
        free(A[i]);
        free(C[i]);
    }
    free(A);
    free(C);

    return result;
}

static PyMethodDef foreign_methods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS, "Возведение матрицы в степень"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",
    "Модуль для возведения матрицы в степень",
    -1,
    foreign_methods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
}
