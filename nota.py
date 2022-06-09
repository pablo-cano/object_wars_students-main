import subprocess


def run_suite(suite):
    process = subprocess.Popen(['pytest', 'test.py', '-vv', '-k', suite],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode('UTF-8')

    return output.count("PASSED")/output.count(suite)


print("""La nota de la actividad se desglosa de la siguiente forma:
    3.5p Tests unitarios
    3.5p Tests de integracion
    2p Tests de funcionalidad
    1p Crear tests
""")
suites = ['Test_unitarios', 'Test_integracion',
          'Test_funcionalidad', 'Test_usuario']
results = [run_suite(suite) for suite in suites]

print(f"""La nota actual de la actividad es:
    {results[0]*3.5}p Tests unitarios
    {results[1]*3.5}p Tests de integracion
    {results[2]*2}p Tests de funcionalidad
    {results[3]}p Crear tests
""")
