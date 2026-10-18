def test_package_imports():
    import {{ package_name }}

    assert {{ package_name }}.__doc__
