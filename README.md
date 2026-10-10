# Toolchain Pinning Free Shell Run Demo

This example demonstrates the 'free shell run' problem where a script's behavior depends on the host environment's PATH and installed tools, leading to inconsistent results. It attempts to execute common command-line tools without explicit checks, illustrating why toolchain pinning is crucial for reliable software.

## Language

`python`

## How to Run

Save the code as main.py.
Run from your terminal: python main.py
Observe how the output changes if 'jq' is not installed or if your default 'python' command points to a different version.

## Original Article

This example accompanies the Turkish article: [Ücretsiz Kabuk Çalıştırmanın Bir Araç Zinciri Sabitlemesi Olmadığına Dair Sıkça Sorulan Sorular](https://fatihsoysal.com/blog/ucretsiz-kabuk-calistirmanin-bir-arac-zinciri-sabitlemesi-olmadigina-dair-sikca-sorulan-sorular/).

## License

MIT — see [LICENSE](LICENSE).
