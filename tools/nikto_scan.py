import subprocess
import os

def run_nikto_scan(target, port, output_format, output_file, additional_params):
    # Build the command with the specified parameters
    command = [
        'nikto', '-host', target,
        '-port', str(port),
        '-Format', output_format,
        '-output', output_file
    ]

    # Add any additional parameters
    if additional_params:
        command.extend(additional_params.split())

    # Run the command
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print("Nikto scan completed successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Nikto: {e}")
        print(e.output)

def main():
    # Get parameters from environment variables
    target = os.getenv('NIKTO_TARGET', 'http://example.com')
    port = int(os.getenv('NIKTO_PORT', '80'))
    output_format = os.getenv('NIKTO_FORMAT', 'txt')
    output_file = os.getenv('NIKTO_OUTPUT', 'nikto_output.txt')
    additional_params = os.getenv('NIKTO_ADDITIONAL', '')

    run_nikto_scan(target, port, output_format, output_file, additional_params)

if __name__ == '__main__':
    main()
