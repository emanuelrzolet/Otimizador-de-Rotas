package com.example.flutter_integration

import android.os.Bundle
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import io.flutter.embedding.android.FlutterActivity
import io.flutter.plugin.common.MethodChannel

class MainActivity: FlutterActivity() {
    private val CHANNEL = "chaquopy"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Configurando o MethodChannel para se comunicar com o Flutter
        MethodChannel(flutterEngine?.dartExecutor?.binaryMessenger, CHANNEL).setMethodCallHandler {
            call, result ->
            if (call.method == "startFletServer") {
                val output = startFletServer()  // Chama a função para iniciar o servidor Python (Flet)
                result.success(output)
            } else {
                result.notImplemented()
            }
        }
    }

    // Função para iniciar o servidor Flet
    private fun startFletServer(): String {
        val py = Python.getInstance()

        // Aqui você chama o script Python (main.py)
        val fletModule: PyObject = py.getModule("main")  // Carrega o arquivo `main.py`
        fletModule.callAttr("main")  // Executa a função `main` dentro do main.py

        return "Servidor Flet Iniciado"
    }
}
