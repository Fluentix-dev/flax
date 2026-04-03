import frontend.typedefinitions.window as window
import frontend.typedefinitions.text_label as text
import frontend.typedefinitions.base as base
import frontend.typedefinitions.image_label as image
import frontend.typedefinitions.button as button

def summon():
    import webbrowser
    webbrowser.open("https://fluentix.dev")

wd = window.Window(1000, 1000, window.WindowAppearanceMode.Light)

# label = text.TextLabel(position=base.Vector2(500, 67), data="SexEngineer loves Dang Xuan Dick", textColor=base.Color(255, 255, 255))
# label.Draw(wd)

# label2 = text.TextLabel(position=base.Vector2(500, 157), data="SexEngineer loves Dang Xuan Dick", textColor=base.Color(255, 255, 255), font=base.Font("Hello, Fluentix!", 14, base.FontStyles.Normal | base.FontStyles.Overstrike), align=base.ElementAlign.NorthEast, useRelativePos=False)
# label2.Draw(wd)
# label2a = text.TextLabel(position=base.Vector2(500, 157), data="SexEngineer loves Dang Xuan Dick", textColor=base.Color(255, 255, 255), font=base.Font("Hello, Fluentix!", 14, base.FontStyles.Normal | base.FontStyles.Overstrike), align=base.ElementAlign.SouthWest, useRelativePos=False)
# label2a.Draw(wd)

# label3 = text.TextLabel(position=base.Vector2(wd.height / 2, wd.width / 2), data="SexEngineer loves Dang Xuan Dick", textColor=base.Color(255, 255, 255), font=base.Font("Hello, Fluentix!", 14, base.FontStyles.Italic | base.FontStyles.Overstrike | base.FontStyles.Bold | base.FontStyles.Underline), align=base.ElementAlign.Center)
# label3.Draw(wd)

sexengineer = text.TextLabel(position=base.Vector2(wd.width / 2, 50), data="This is the lover of Dang Xuan Dick", font=base.Font("Hello, Fluentix!", 30, base.FontStyles.Bold | base.FontStyles.Italic))
sexengineer2 = text.TextLabel(position=base.Vector2(wd.width / 2, 100), data="SexEngineer", font=base.Font("Hello, Fluentix!", 15, base.FontStyles.Italic))


sexengineer.Draw(wd)
sexengineer2.Draw(wd)

summon_sex_engineer = button.Button(position=base.Vector2(100, 100), color=base.Color(255, 0, 0), hoverColor=base.Color(0, 255, 255), activationFunction=summon, buttonSize=base.Vector2Int(200, 200), textLabel="Fluentix Homepage", textLabelColor=base.Color(255, 255, 255))
summon_sex_engineer.Draw(wd)

wd.Run()
