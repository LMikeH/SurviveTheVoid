from cx_Freeze import setup, Executable

base = "Win32GUI"

additional_mods = ['numpy.core._methods',
                   'numpy.lib.format',
                   ]

assets = ['assets/']

setup(name="SurviveTheVoid",
      version="0.1",
      options={"build_exe": {'packages': ['scipy', 'numpy'],
                            'includes': additional_mods,
                            # 'include_files': assets
                             }
               },
      executables=[Executable("__main__.py",
                              base=base,
                              targetName="SurviveTheVoid.exe")]
      )
