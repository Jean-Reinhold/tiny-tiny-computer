from assembler.assemble import two_pass_assemble

if __name__ == "__main__":
    file_to_assemble = "sample.asm"
    ok = two_pass_assemble(file_to_assemble)
    if ok:
        print("Montagem completada com sucesso!")
    else:
        print("Ocorreram erros durante a montagem.")
